"""Simple Api.

The purpose of this api is to demonstrate
FlaskRest-full
"""
import os
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.user import RegisterUser
from security import authenticate, identity
from resources.item import Item, ItemsList
from resources.store import Store, StoreItem


app = Flask(__name__)
api = Api(app)
app.secret_key = "hello key"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
jwt = JWT(app, authenticate, identity)


api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/Item/<string:name>")
api.add_resource(ItemsList, "/Items")
api.add_resource(RegisterUser, "/register")
api.add_resource(StoreItem, "/stores")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
