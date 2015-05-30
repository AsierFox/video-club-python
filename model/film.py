
class Film():
    name = ""
    code = 0
    last_film = 0
    available = False

    def __init__(self, name, code, last_film, available):
        self.name = name
        self.code = code
        self.last_client = last_film
        self.available = available