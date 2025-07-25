from server.config import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    __tablename__ = "resturant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'),nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    @validates('price')
    def validate_price(self, key, value):
        if not (1 <= value <= 30):
            raise ValueError("Price must be between 1 and 30")
        return value
    def __repr__(self):
        return f"RestaurantPizza {self.price}"