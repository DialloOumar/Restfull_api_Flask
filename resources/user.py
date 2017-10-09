"""Creating users.

This module is responsible for creating users in our system as objects

"""

from models.user_model import UserModel

from flask_restful import Resource, reqparse


class RegisterUser(Resource):
    """Sign up

    This Resource is for signing up users
    """

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field connot be empty"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field connot be empty"
    )

    def post(self):
        """
        This endpoint is responsible for getting username and password
        :return: void
        """

        data = RegisterUser.parser.parse_args()

        username = data["username"]

        if UserModel.find_by_username(username):
            return {'message': "This user already exist"}, 400

        user = UserModel(**data)

        print(user.save_to_db())

        return {"message": "Registration successful"}, 201
