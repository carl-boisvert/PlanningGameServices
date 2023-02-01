from flask import Blueprint, make_response, jsonify, request

import services.player_service as PlayerService

player_controller = Blueprint('player_controller', __name__)


@player_controller.route("/player/steam/<string:steam_id>", methods=["GET"])
def player_steam_login(steam_id):
    user = PlayerService.get_user(steam_id)
    if user is None:
        return make_response(jsonify({}), 404)
    return jsonify(user)


@player_controller.route("/player/steam", methods=["POST"])
def create_player_steam():
    content = request.get_json()
    if content["steam_id"] is not None and content["gamertag"] is not None:
        user = PlayerService.create_user(content["steam_id"], content["gamertag"])
        return jsonify(user)
    else:
        make_response({}, 403)


@player_controller.route("/player/steam/<string:steam_id>", methods=["DELETE"])
def delete_player_steam(steam_id):
    PlayerService.delete_user(steam_id)
    return make_response({}, 200)


@player_controller.route("/player/steam/currency", methods=["POST"])
def player_add_currency():
    content = request.get_json()
    if content.keys() >= {"steam_id", "amount"}:
        PlayerService.add_currency(content["steam_id"], content["amount"])
    else:
        return make_response({"error":"missing arguments"}, 403)
    return make_response({}, 200)
