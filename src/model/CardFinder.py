"""
Clase CardFinder
####################
Encuentra el PATH de cada carta y le asigna un ID.
"""


import os


class CardFinder:
    def __init__(self):
        self.__BASEPATH = os.path.abspath(os.path.dirname("__file__"))

    def getCardFolder(self):
        """
        Busca el directorio que contiene a las imágenes

        :return: PATH del directorio.
        :rtype: str
        """
        dirs = os.listdir(self.__BASEPATH)

        for dir in dirs:
            if dir == "img":
                return os.path.join(self.__BASEPATH, "img")

    def getCardPathIds(self):
        """
        Retorna un diccionario que contiene PATH y ID.

        :return: Diccionario con cartas.
        :rtype: dict
        """
        cardDict = {}

        (_, _, cardsList) = next(os.walk(self.getCardFolder()))

        for card in cardsList:
            cardId = card.split(".")[0]
            cardPath = os.path.join(self.getCardFolder(), card)

            if not cardId == "back":
                cardDict[cardId] = cardPath

        return cardDict
