import os

from flask import Flask, jsonify, request

from dotenv import load_dotenv
from flask_dotenv import DotEnv
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

from services.user_service import UserService


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

env = DotEnv()
env.init_app(app, os.path.join(basedir, '.env'))

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

app.config['MONGODB_SETTINGS'] = {
    "db": "GameService",
}
db = MongoEngine(app)
jwt = JWTManager(app)

@app.route('/steam/login/<string:steam_id>')
def steam_login(steam_id):  # put application's code here
    user_service = UserService(db)
    user = user_service.get_user(steam_id)
    if user is None:
        user = user_service.create_user("steam_id", "Snappydue")
    return jsonify(user)


if __name__ == '__main__':
    app.run()
