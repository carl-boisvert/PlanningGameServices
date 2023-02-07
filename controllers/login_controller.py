from flask import Blueprint, request, make_response, jsonify

import services.steam_service as SteamService
from models.player import Player

login_controller = Blueprint('login_controller', __name__)

@login_controller.route("/login/steam", methods=["POST"])
def player_steam_login():
    session_ticket = request.form.get("SessionTicket")
    player = None
    if session_ticket:
        steam_id = SteamService.login(session_ticket)
        player = Player.objects(steam_id=steam_id).first()
        if player is None:
            gamertag = SteamService.get_player_gamertag(steam_id)
            player = Player(steam_id=steam_id, gamertag=gamertag)
            player.save()
    return jsonify(player)
