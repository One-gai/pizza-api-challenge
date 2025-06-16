import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.config import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.app import app  # Make sure app is imported so db knows the context

with app.app_context():
    print("🌱 Seeding data...")

    # Clear old data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create Pizzas
    pepperoni = Pizza(name="Pepperoni", ingredients="Cheese, Tomato, Pepperoni")
    veggie = Pizza(name="Veggie", ingredients="Cheese, Tomato, Peppers, Onions, Olives")
    bbq = Pizza(name="BBQ Chicken", ingredients="Chicken, BBQ Sauce, Cheese")

    # Create Restaurants
    mama_mias = Restaurant(name="Mama Mia's", address="123 Main Street")
    pizza_palace = Restaurant(name="Pizza Palace", address="456 Broadway Ave")

    # Add pizzas and restaurants to the session
    db.session.add_all([pepperoni, veggie, bbq, mama_mias, pizza_palace])
    db.session.commit()

    # Create RestaurantPizza relationships
    rp1 = RestaurantPizza(price=12, pizza_id=pepperoni.id, restaurant_id=mama_mias.id)
    rp2 = RestaurantPizza(price=10, pizza_id=veggie.id, restaurant_id=mama_mias.id)
    rp3 = RestaurantPizza(price=14, pizza_id=bbq.id, restaurant_id=pizza_palace.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Done seeding!")
