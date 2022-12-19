import sys
import json
from datetime import datetime, timedelta

from flask_login import UserMixin

from ..common.exec import run_authnz_db


class User(UserMixin):
    def __init__(self, user_id=None, name=None, email=None):
        print("Running User.__init__", file=sys.stderr)
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = None
        self.token = None
        self.token_expiration = None

    @staticmethod
    def get(user_id=None,token=None):
        print("running User.get(user_id='%s',token='%s')" % (user_id,token), file=sys.stderr)

        if user_id is not None:        
            res = run_authnz_db(["authnz-db", "user", "get", user_id])
            js = json.loads(res.stdout)
            print("js: '%s'" % js, file=sys.stderr)
            foo = User().populate(js[0])
            print("foo: '%s'" % foo, file=sys.stderr)
            return foo

        # get user_id from token
        if token is not None:
            print("Getting user from token '%s'" % token, file=sys.stderr)
            res = run_authnz_db(["authnz-db","user","token","get",token])
            js = json.loads(res.stdout)
            return User().populate(js[0])

        raise Exception("You must pass either user_id or token")

    @staticmethod
    def check_password(user_id, password):
        print("running User.check_password('%s')" % password, file=sys.stderr)
        run_authnz_db(["authnz-db", "user", "auth", user_id, password])
        return True

#    @staticmethod
#    def create(obj):
#        obj = User()
#        obj.populate(user_id=user_id, name=name, email=email, password=password)
#        print("running User.create('%s')" % user_id, file=sys.stderr)
#        a = ["authnz-db", "user", "create", "-u", user_id]
#        a.append(["-n", name, "-e", email, "-p", password])
#        res = subprocess.run(a)
#        if res.returncode != 0 or len(res.stdout) < 1:
#            return None
#        return self

    def populate(self, obj):
        print("populate: '%s'" % obj, file=sys.stderr)
        if 'user_id' in obj and obj['user_id'] is not None:
            self.user_id = obj['user_id']
        if 'name' in obj and obj['name'] is not None:
            self.name = obj['name']
        if 'email' in obj and obj['email'] is not None:
            self.email = obj['email']
        if 'password' in obj and obj['password'] is not None:
            self.password = obj['password']
        if 'token' in obj and obj['token'] is not None:
            self.token = obj['token']
        if 'token_expiration' in obj and obj['token_expiration'] is not None:
            self.token_expiration = obj['token_expiration']
        return self

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        # db.session.add(self)
        run_authnz_db(["authnz-db","user","token","update",self.user_id,self.token,self.token_expiration])
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)
        run_authnz_db(["authnz-db","user","token","update",self.user_id,self.token,self.token_expiration])

    @staticmethod
    def check_token(token):
        user = User.get(token=token)
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

