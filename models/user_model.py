"""
Model for manipulating users
"""
import sqlite3
from db import db


class UserModel(db.Model):
    """User.

    This is the user class

    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        """Constructor.

        This is the constructor for initializing our user objects
        """
        self.username = username
        self.password = password

    def save_to_db(self):
        """
        Method Responsible for inserting a new user
        :return: inserted user
        """
        db.session.add(self)
        db.session.commit()

    def get_json(self):
        return {"username": self.username, "password": self.password}

    @classmethod
    def find_by_username(cls, username):
        """Fetch Data.

        Method for fetching users by username
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        """Fetch Data.

        This function is allowed to get the
        """
        return cls.query.filter_by(id=_id).first()


