
import json
import subprocess
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id=None, name=None, email=None):
        self.user_id = user_id
        self.name = name
        self.email = email

    def get(self, user_id):
        if self.id_ == None: 
            self.user_id = user_id
        res = subprocess.run(["authns-db", "user", "get", user_id], capture_output=True)
        if res.returncode != 0 or len(res.stdout) < 1:
            return None
        js = json.loads(res.stdout)
        self.name = js['name']
        self.email = js['email']
        return self

    def check_password(self, password):
        res = subprocess.run(
            ["authns-db", "user", "auth", self.user_id, password],
            capture_output=True
        )
        if res.returncode != 0 or len(res.stdout) < 1:
            return None
        return self

    def create(self, user_id, name, email, password):
        if self.user_id == None:
            self.user_id = user_id
            self.name = name
            self.email = email
        res = subprocess.run(
            ["authns-db", "user", "create", "-u", user_id, "-n", name, "-e", email, "-p", password]
        )
        if res.returncode != 0 or len(res.stdout) < 1:
            return None
        return self
