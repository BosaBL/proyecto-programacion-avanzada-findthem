import os


class CardFinder:
    def __init__(self):
        self.__BASEPATH = os.path.abspath(os.path.dirname("__file__"))

    def getCardFolder(self):
        dirs = os.listdir(self.__BASEPATH)

        for dir in dirs:
            if dir == "img":
                return os.path.join(self.__BASEPATH, "img")

    def getCardPathIds(self):

        cardDict = {}

        (_, _, cardsList) = next(os.walk(self.getCardFolder()))

        for card in cardsList:
            cardId = card.split(".")[0]
            cardPath = os.path.join(self.getCardFolder(), card)

            cardDict[cardId] = cardPath

        return cardDict
