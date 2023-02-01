import mongoengine as me

class Player(me.Document):
    skins = me.ListField(default=[])
    gamertag = me.StringField(required=True)
    steam_id = me.StringField(required=True, unique=True)
    currency_amount = me.IntField(default=0)