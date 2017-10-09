
from flask_restful import Resource, reqparse
from flask_jwt import  jwt_required
from models.store_model import StoreModel


class Store(Resource):
    """
    This resource contains all the operations that will be performed on
    a store operations like adding a store, updating an existing store,
    deleting an existing store, or getting a particular store

    However, it does not take care of getting all the stores created
    """
    @jwt_required()
    def get(self, name):
        """
        Getting a store its name
        :param name:
        :return:
        """
        store = StoreModel.find_item(name)

        if store is None:
            return {"message": "store does not exist"}, 404
        return store.json()

    def post(self, name):
        """
        This function adds a new store to the database. However, before
        adding a store we must make sure that the store we intend to add
        does not exist if it does we return to the client that the store
        already exist
        :param name:
        :return:
        """
        store = StoreModel.find_item(name)

        if store is not None:
            return {"message": "Store already exist"}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "An error occured while inserting store"}, 500

        return store.json(), 201

    def delete(self, name):
        """
        This function is responsible for deleting a store if the store
        exist if not it will return that the store the user intend to
        delete does not exist
        :param name:
        :return:
        """
        store = StoreModel.find_item(name)

        if store:
            store.delete_from_db()
            return {"message": "store deleted"}

        return {"message": "The store you are trying to delete does not exist"}, 400


class StoreItem(Resource):
    """
    This resource is for getting the list off all the available stores
    with each store will be associated with the items it contains
    """
    def get(self):
        """
        Gettng all the store
        :return:
        """
        return {"stores": [store.json() for store in StoreModel.query.all()]}
