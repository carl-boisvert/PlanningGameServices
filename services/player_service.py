from flask_pymongo import PyMongo

from models.player import Player


def add_currency(steam_id, amount):
    user = Player.objects(steam_id=steam_id).first()
    new_currency_amount = min(user.currency_amount+amount, 999)
    user = user.update(currency_amount=new_currency_amount)
    return user


def create_user(steam_id, gamertag):
    user = Player(steam_id=steam_id, gamertag=gamertag)
    user = user.save()
    return user


def get_user(steam_id):
    user = Player.objects(steam_id=steam_id).first()
    return user


def delete_user(steam_id):
    user = Player.objects(steam_id=steam_id).first()
    user.delete()
    return


