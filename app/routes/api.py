from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import os

api_bp = Blueprint('api', __name__)
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client.chatapp

@api_bp.route('/messages', methods=['GET'])
def get_messages():
    messages = list(db.messages.find({}, {'_id': 0}))
    return jsonify(messages)

@api_bp.route('/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    db.messages.insert_one(data)
    return jsonify({"status": "Message received"}), 201