from werkzeug.security import safe_str_cmp
from user import User


def authenicate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    print(payload)
    return User.find_by_id(user_id)