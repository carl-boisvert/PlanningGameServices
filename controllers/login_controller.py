from flask import Blueprint, make_response, jsonify

from services.user_service import UserService

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/steam/login/<string:steam_id>')
def steam_login(steam_id):  # put application's code here
    user_service = UserService()
    user = user_service.get_user(steam_id)
    if user is None:
        return make_response(jsonify({}), 404)
    return jsonify(user)