"""!
Clase CardFinder
Encargada de encontrar la ruta de cada carta.
"""
import os


class CardFinder:
    def __init__(self):
        self.__BASEPATH = os.path.abspath(os.path.dirname("__file__"))

    ##
    # @return path str: ruta de la carpeta donde se encuentran las cartas.
    def getCardFolder(self):
        dirs = os.listdir(self.__BASEPATH)

        for dir in dirs:
            if dir == "img":
                return os.path.join(self.__BASEPATH, "img")

    ##
    # @return dict{id:"path"}: iccionario con la id y path de cada carta.
    def getCardPathIds(self):

        cardDict = {}

        (_, _, cardsList) = next(os.walk(self.getCardFolder()))

        for card in cardsList:
            cardId = card.split(".")[0]
            cardPath = os.path.join(self.getCardFolder(), card)

            if not cardId == "back":
                cardDict[cardId] = cardPath

        return cardDict
