import mongoengine as me

class User(me.Document):
    _id = me.ObjectIdField()
    skin = me.ListField(default=[])
    gamertag = me.StringField(required=True)
    steam_id = me.StringField(required=True, unique=True)
