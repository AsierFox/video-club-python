
import db.db as db


def start():
    clientData = db.Database('clients.txt')
    filmData = db.Database('films.txt')

    client_list = clientData.open_connection()
    film_list = filmData.open_connection()

    clientData.close_connection()
    filmData.close_connection()