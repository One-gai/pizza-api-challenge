# 🍕 Pizza API Challenge

A Flask-based RESTful API that manages Pizzas, Restaurants, and the prices they charge at each restaurant.

---

## 🧰 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge
Install dependencies using Pipenv

bash
Copy
Edit
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
Set Flask app environment variable

bash
Copy
Edit
export FLASK_APP=server/app.py
Run database migrations

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the database

Add sample data in server/seed.py

Then run:

bash
Copy
Edit
python server/seed.py
🗂 Route Summary
Method	URL	Description
GET	/restaurants	List all restaurants
GET	/restaurants/<id>	Get a specific restaurant with its pizzas
DELETE	/restaurants/<id>	Delete a restaurant
GET	/pizzas	List all pizzas
POST	/restaurant_pizzas	Associate a pizza with a restaurant

📬 Example Requests & Responses
GET /restaurants
json
Copy
Edit
[
  {
    "id": 1,
    "name": "Mama Mia's",
    "address": "123 Main Street"
  }
]
GET /restaurants/1
json
Copy
Edit
{
  "id": 1,
  "name": "Mama Mia's",
  "address": "123 Main Street",
  "pizzas": [
    {
      "id": 1,
      "name": "Pepperoni",
      "ingredients": "Cheese, Tomato, Pepperoni"
    }
  ]
}
POST /restaurant_pizzas
Request Body:
json
Copy
Edit
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 1
}
Response:
json
Copy
Edit
{
  "id": 4,
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 1,
  "pizza": {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Cheese, Tomato, Pepperoni"
  },
  "restaurant": {
    "id": 1,
    "name": "Mama Mia's",
    "address": "123 Main Street"
  }
}
✅ Validation Rules
price must be an integer between 1 and 30

pizza_id and restaurant_id must be valid existing IDs

JSON must be well-formatted and included in POST requests

🧪 Postman Usage Instructions
Start your Flask server

bash
Copy
Edit
flask run
Open Postman and set up a new request:

Method: POST

URL: http://localhost:5000/restaurant_pizzas

Headers:
Content-Type: application/json

Body (raw → JSON):

json
Copy
Edit
{
  "price": 20,
  "pizza_id": 2,
  "restaurant_id": 1
}
Send request and view the JSON response.

📌 Status
✔ MVP completed
✔ API routes working
✔ JSON responses validated
✔ Postman tested