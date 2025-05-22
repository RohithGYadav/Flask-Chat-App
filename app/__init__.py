from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from pymongo import MongoClient
import os

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'secret!'
    app.config['MONGO_URI'] = os.getenv("MONGO_URI", "mongodb://localhost:27017/chatapp")

    from .routes.api import api_bp
    from .routes.views import views_bp
    from .sockets.chat import register_socket_events

    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(views_bp)

    socketio.init_app(app)
    register_socket_events(socketio)

    return app