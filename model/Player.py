"""!
Clase Player
Encarga de modelar un jugador.
"""


class Player:
    def __init__(self, name: str, points: int):
        self.__name = name
        self.__points = points

    ## @returns name str: nombre del jugador.
    def getName(self):
        return self.__name

    ## @returns points int: puntos del jugador.
    def getPoints(self):
        return self.__points

    ## Añade puntos al jugador
    # @param points int: puntos.
    def addPoints(self, points: int):
        self.__points += points

    ## Reinicia los puntos del jugador.
    def resetPoints(self):
        self.__points = 0
