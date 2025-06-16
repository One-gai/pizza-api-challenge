from server.config import db
from flask_sqlalchemy import SQLAlchemy


class Restaurant(db.Model):
    __tablenname__ = 'Restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref = 'restaurant', cascade ='all, delete-orphan')

    def __repr__(self):
        return f"Restaurant {self.name}"