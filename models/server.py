from enum import Enum

import mongoengine as me


class ServerStatus(Enum):
    STARTING = "STARTING"
    WAITING_FOR_PLAYERS = "WAITING_FOR_PLAYERS"
    IN_GAME = "IN_GAME"
    SHUTDOWN = "SHUTDOWN"



class Server(me.Document):
    ip_address = me.StringField(required=True)
    status = me.StringField(default=ServerStatus.STARTING.value)

