
class Client():
    name = ""
    code = 0
    last_client = None
    available = False

    def __init__(self, name, code, last_client, available):
        self.name = name
        self.code = code
        self.last_client = last_client
        self.available = available