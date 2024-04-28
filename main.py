from flask import Flask, request, jsonify
from pymongo import MongoClient
import json 
from bson import json_util

app = Flask(__name__)
cluster = MongoClient("mongodb+srv://rovonod596:qDHxMuczWqT4jJfv@cluster0.c0szyw0.mongodb.net/")
db = cluster["basic_app"]
collection = db["credentials"]

# collection.insert_one({"seed": "check"})

@app.route("/add_login_info", methods=["POST"])
def add_login_info():
    data = request.json
    if data:
        collection.insert_one(data)
        return jsonify({"message": "Data added successfully"}), 201
    else:
        return jsonify({"error": "No data provided"}), 400

@app.route("/login_info", methods=["GET"])
def get_login_details():
    all_details = list(collection.find())
    return json.dumps(all_details, default=json_util.default)


if __name__ == "__main__":
    app.run(debug=True)
