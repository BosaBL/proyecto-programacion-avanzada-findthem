"""
Clase DatabaseController
#######################
Controlador de :py:class:`model.Database`
"""
from model.Database import Database


class DatabaseController:
    def __init__(self):
        self.__database = Database()

    def databaseConnection(self):
        """
        Establece una conección con la base de datos.
        """
        return self.__database

    def descOrder(self):
        """
        :return: lista ordenada en manera descendente de los jugadores.
        :rtype: list[dict]
        """
        list = self.__database.readScoreBoard()
        list.sort(key=lambda x: int(x["Points"]), reverse=True)
        return list
