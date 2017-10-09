"""Security Module.

This module is used for providing proper user authentication
"""

from resources.user import UserModel


def authenticate(username, password):
    """Authicate user.

    This function is in charge of the authentication. The function
    returns the user if the username and password matches.
    """
    # user = user_mapping.get(username, None)
    user = UserModel.find_by_username(username)

    print("authentication: " + str(user))
    if user and user.password == password:
        print("authentication: " + str(user))
        return user


def identity(payload):
    """Remember User.

    This function
    """
    user_id = payload["identity"]

    return UserModel.find_by_id(user_id)
