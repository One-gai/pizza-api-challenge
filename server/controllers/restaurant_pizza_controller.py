
from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.config import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    if not data:
        return jsonify({ "error": "No JSON received or invalid format." }), 400
    
    try:
        price = int(data.get('price'))
        pizza_id = int(data.get('pizza_id'))
        restaurant_id = int(data.get('restaurant_id'))

        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_rp)
        db.session.commit()

        return jsonify({
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza_id": new_rp.pizza_id,
            "restaurant_id": new_rp.restaurant_id,
            "pizza": {
                "id": new_rp.pizza.id,
                "name": new_rp.pizza.name,
                "ingredients": new_rp.pizza.ingredients
            },
            "restaurant": {
                "id": new_rp.restaurant.id,
                "name":new_rp.restaurant.name,
                "address": new_rp.restaurant.address
            }
        }), 201
    except ValueError as ve:
        return jsonify({ "errors": [str(ve)]}), 400
    
    except Exception as e:
        return jsonify({ "errors": ["Invalid data"]}), 400
    