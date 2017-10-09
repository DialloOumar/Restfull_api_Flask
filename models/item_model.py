from db import db


class ItemModel(db.Model):
    """
    This model is responsible for the operations performed on an item
    """

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float)

    store_id = db.Column(db.ForeignKey("stores.id"))

    store = db.relationship("StoreModel")

    def __init__(self, name, price, store_id):
        """
        Constructor initialization
        :param name:
        :param price:
        """
        self.name = name
        self.price = price
        self.store_id = store_id

    def save_to_db(self):
        """
        Responsible for both adding and updating the database
        :return:
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Method responsible for deleting an item in the database
        :return:
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_item(cls, name):
        """
        Retrieve an item from the database base on the items name
        :param name:
        :return:
        """
        return cls.query.filter_by(name=name).first()

    def json(self):
        return {"name": self.name, "price": self.price, "store_id": self.store_id}
