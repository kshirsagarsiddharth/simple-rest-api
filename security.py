from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


def identity(palyload):
    user_id = palyload['identity']
    return UserModel.find_by_id(user_id)
