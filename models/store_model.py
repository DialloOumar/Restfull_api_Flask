from db import db


class StoreModel(db.Model):
    """
    This model is responsible for the operations performed on an item
    """

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship("ItemModel")

    def __init__(self, name):
        """
        Constructor initialization
        :param name:
        :param price:
        """
        self.name = name

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
        return {"name": self.name, "items": [item.json() for item in self.items]}
