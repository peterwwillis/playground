import sys
import json
import subprocess
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id=None, name=None, email=None):
        print("Running User.__init__", file=sys.stderr)
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = None

    def get(self, user_id=None):
        self.populate(user_id=user_id)
        print("running User.get('%s')" % self.user_id, file=sys.stderr)
        res = subprocess.run(
            ["authnz-db", "user", "get", self.user_id], capture_output=True
        )  # noqa
        if res.returncode != 0 or len(res.stdout) < 1:
            return None
        js = json.loads(res.stdout)
        self.name = js["name"]
        self.email = js["email"]
        return self

    def check_password(self, password):
        print("running User.check_password('%s')" % password, file=sys.stderr)
        res = subprocess.run(
            ["authnz-db", "user", "auth", self.user_id, password],
            capture_output=True,  # noqa
        )  # noqa
        if res.returncode != 0 or len(res.stdout) < 1:
            return None
        return self

    def create(self, user_id=None, name=None, email=None, password=None):
        self.populate(user_id=user_id, name=name, email=email, password=password)
        print("running User.create('%s')" % user_id, file=sys.stderr)
        a = ["authnz-db", "user", "create", "-u", user_id]
        a.append(["-n", name, "-e", email, "-p", password])
        res = subprocess.run(a)
        if res.returncode != 0 or len(res.stdout) < 1:
            return None
        return self

    def populate(self, user_id=None, name=None, email=None, password=None):
        if self.user_id is None and user_id is not None:
            self.user_id = user_id
        if self.name is None and name is not None:
            self.name = name
        if self.email is None and email is not None:
            self.email = email
        if self.password is None and password is not None:
            self.password = password

