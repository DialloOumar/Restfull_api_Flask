
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item_model import ItemModel


class Item(Resource):
    """First Api.

    Responsible for.

    """
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every item must have a store id "
    )

    @jwt_required()
    def get(self, name):
        """Get name.

        GET a particular item based on it unique name
        """
        item = ItemModel.find_item(name)

        if item:
            return item.json()

        return {"message": "item not foud"}, 400

    def post(self, name):
        """Create an Item.
        This endpoint is responsible for creating an item. If creation
        is successful it will return 201 else it will return 409 for duplicate entry
        """
        data = Item.parser.parse_args()

        item = ItemModel.find_item(name)

        if item:
            return {"message": "item already exist"}, 403

        new_item = ItemModel(name, **data)
        new_item.save_to_db()

        return new_item.json(), 201

    def delete(self, name):

        """Delete an existing item.

        This function is responsible for deleting an item form our items
        list
        """
        item = ItemModel.find_item(name)

        if item is None:
            return {"message": "The item does not exist"}
        item.delete_from_db()

        return {"message": "item deleted successfully"}

    def put(self, name):
        """Update an Item.
        This function is meant for updating an existing item
        """

        request_data = Item.parser.parse_args()

        item = ItemModel.find_item(name)

        if item is None:

            item = ItemModel(name, **request_data)
        else:

            item.price = request_data["price"]

        item.save_to_db()

        return item.json(), 201


class ItemsList(Resource):
    """All items list.

    This resource is for getting the list of all available items

    """

    def get(self):
        """Get The list.

        This Endpoint is for getting all items
        """
        return {"items": [item.json() for item in ItemModel.query.all()]}
