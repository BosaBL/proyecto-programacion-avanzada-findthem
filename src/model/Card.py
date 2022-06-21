"""
Clase Card
#################
Modelo de una Carta del juego
"""


class Card:
    """
    :param identifier: identificador o ID de la carta.
    :param path: OS PATH de la imagen de la carta.
    :type identifier: int
    :type path: str
    """

    def __init__(self, identifier: int, path: str):
        self.__id = identifier
        self.__imagePath = path

    def getId(self):
        """
        :return: Identificador de la carta.
        :rtype: int
        """
        return self.__id

    def getPath(self):
        """
        :return: path de la carta.
        :rtype: str
        """
        return self.__imagePath
