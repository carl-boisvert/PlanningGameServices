import os

from flask import Flask, jsonify, make_response

from dotenv import load_dotenv
from flask_dotenv import DotEnv
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

from controllers.player_controller import player_controller
from middleware.format_response import format_response_middleware

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

env = DotEnv()
env.init_app(app, os.path.join(basedir, '.env'))

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

app.config['MONGODB_SETTINGS'] = {
    "db": "GameService",
    "host": os.getenv('MONGO_URI'),
    "port": 27017
}
db = MongoEngine(app)
jwt = JWTManager(app)

app.register_blueprint(player_controller)
app.after_request(format_response_middleware)

if __name__ == '__main__':
    app.run()
