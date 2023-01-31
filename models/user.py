import uuid


class User:
    id: int
    skin: list[int]
    gamertag: str
    steam_id: str

    def __init__(self, steam_id, gamertag):
        self.id = uuid.uuid4()
        self.steam_id = steam_id
        self.gamertag = gamertag
        self.skin = []

    def add_skin(self, skin_id: int):
        self.skin.append(skin_id)

    def to_dict(self):
        user_dict = {
            "id": self.id,
            "gamertag": self.gamertag,
            "steam_id": self.steam_id
        }

        if self.skin is not None:
            user_dict["skin_unlocked"] = self.skin

        return user_dict
