import json
import time

from flask import Flask, request, jsonify

app = Flask(__name__)

# Load seeded data from seed.json
try:
    with open('seed.json', 'r') as f:
        raw_users = json.load(f)
        # Convert keys to match internal structure
        users = [
            {
                "id": u["id"],
                "username": u["doggy"],
                "password": u["zebra42"],
                "email": u["kittycat"],
                "age": u["rocketShip"]
            } for u in raw_users
        ]
except FileNotFoundError:
    users = []


# GET: Return all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200
HEAD

# POST: Add a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,



# POST: Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    required = ["username", "password", "email", "age"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    new_id = max([u["id"] for u in users], default=0) + 1

    new_user = {
        "id": new_id,
52b22dc (Completed Flask CRUD puzzle)
        "username": data["username"],
        "password": data["password"],
        "email": data["email"],
        "age": data["age"]
    }
HEAD


52b22dc (Completed Flask CRUD puzzle)
    users.append(new_user)
    return jsonify(new_user), 201



# PUT: Update user by ID
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
HEAD
    for user in users:
        if user["id"] == user_id:
            user["username"] = data["username"]
            user["password"] = data["password"]
            user["email"] = data["email"]
            user["age"] = data["age"]
            return jsonify(user), 200

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    for u in users:
        if u["id"] == user_id:
            u["username"] = data.get("username", u["username"])
            u["password"] = data.get("password", u["password"])
            u["email"] = data.get("email", u["email"])
            u["age"] = data.get("age", u["age"])
            return jsonify(u), 200

52b22dc (Completed Flask CRUD puzzle)
    return jsonify({"error": "User not found"}), 404



# DELETE: Remove user by ID
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
HEAD
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

    for i, u in enumerate(users):
        if u["id"] == user_id:
            deleted = users.pop(i)
            return jsonify(deleted), 200

    return jsonify({"error": "User not found"}), 404
52b22dc (Completed Flask CRUD puzzle)



# starts the application, and binds to 127.0.0.1 NOT localhost!!!
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
