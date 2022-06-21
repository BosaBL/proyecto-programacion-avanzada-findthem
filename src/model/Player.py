"""
Clase Player
#################
Otorga un modelo de jugador.
"""


class Player:
    """
    :param name: nombre del jugador.
    :type name: str
    :param points: puntos del jugador
    :type points: int
    """

    def __init__(self, name: str, points: int):
        self.__name = name
        self.__points = points

    def getName(self):
        """
        :return: nombre del jugador.
        :rtype: str
        """
        return self.__name

    def getPoints(self):
        """
        :return: puntaje del jugador.
        :rtype: int
        """
        return self.__points

    def addPoints(self, points: int):
        """
        Añade puntos a un jugador.

        :param points: puntos a añadir.
        :type points: int
        """
        self.__points += points

    def resetPoints(self):
        """
        Reinicia los puntos del jugador a 0.
        """
        self.__points = 0
