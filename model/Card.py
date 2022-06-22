"""!
Clase Card
Encargada de modelar una carta.
"""


class Card:
    ##
    # @param identifier int: identificador de la carta.
    # @param path str: ruta de la carta.
    def __init__(self, identifier: int, path: str):
        self.__id = identifier
        self.__imagePath = path

    ##
    # @return id int: devuelve id de la carta.
    def getId(self):
        return self.__id

    ##
    # @return path str: devuelve la ruta de la carta.
    def getPath(self):
        return self.__imagePath
