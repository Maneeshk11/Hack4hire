from flask import Flask, jsonify, request
from pymongo import MongoClient
import bson
from bson import json_util
from datetime import datetime
import logging
import sys
import uuid
import json

def printf(x):
    print(x, file=sys.stderr)
    #app.logger.info(x)
printf("Running!")
def parse_json(data):
    return json.loads(json_util.dumps(data))

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# with collection.watch() as stream:
#     for change in stream:
#         printf(change)

collection.delete_many({})

unique_id = str(uuid.uuid4())
my_data = {
        "id": unique_id,
        'title' :  'Gym',
        'description' : 'Hit the Gym',
        'date' : "2023-04-01",
        'duration' : '2',
        'deadline' : "2023-04-01",
        'type' : 'Personal'
}


collection.insert_one(my_data)
unique_id = str(uuid.uuid4())
my_data = {
        "id": unique_id,
        'title' :  'Machine Learning Project',
        'description' : 'Implementing exchange rate prediction using different regression models and choosing the best from them',
        'date' : "2023-04-01",
        'duration' : '8',
        'deadline' : "2023-04-10",
        'type' : 'Personal'
}

collection.insert_one(my_data)

printf(collection)

@app.route("/")
def route():
    return "Hello World!"

@app.route("/api/create", methods=["POST", "GET"])
def create():
    data = request.json
    unique_id = str(uuid.uuid4())
    deadline = datetime.strptime(data["deadline"], "%Y-%m-%d")
    my_data = {   
                    "id": unique_id,
                    "title": data["title"],
                    "description": data["description"],
                    "duration": data["duration"],
                    "date": datetime.today().replace(microsecond=0),
                    "deadline": deadline,
                    "type": data["type"]
                }
    collection.insert_one(my_data)
    return "Data inserted successfully!"

@app.route("/api/read", methods=["POST", "GET"])
def read():
    data = []
    printf(collection.find())
    blocks = collection.find()

    data = []
    for block in blocks:
        data.append(block)
    printf(data)
    json_data = parse_json(data)

    # Print the JSON string
    print(json_data)
    return {"data":json_data}

@app.route("/api/update", methods=["POST", "GET"])
def update():
    data = request.json
    my_query = {
        "id": data["id"]}
    
    new_values = {"$set": {
        "title": data["title"],
        "description": data["description"],
        "duration": data["duration"],
        "date": data["date"],
        "deadline": data["deadline"],
        "type": data["type"]
    }}

    collection.update_one(my_query, new_values)
    return "Updated successfully"

@app.route("/api/delete", methods=["POST", "GET"])
def delete():
    data = request.json
    my_query = {"id": data["id"]}
    collection.delete_one(my_query)
    return "Data deleted successfully!"

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
