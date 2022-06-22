"""!
Controlador de model.Database
"""
from model.Database import Database


class DatabaseController:
    def __init__(self):
        self.__database = Database()

    ##
    # @return database(): conexión con la base de datos.
    def databaseConnection(self):
        return self.__database

    ##
    # return list[jugadores]: lista ordenada de forma descendente de Player.
    def descOrder(self):
        list = self.__database.readScoreBoard()
        list.sort(key=lambda x: int(x["Points"]), reverse=True)
        return list
