from flask_pymongo import PyMongo

from models.user import User

class UserService():
    def create_user(self, steam_id, gamertag):
        user = User(steam_id=steam_id, gamertag=gamertag)
        user.save()
        return user

    def get_user(self, steam_id):
        user = User.objects(steam_id=steam_id).first()
        return user

