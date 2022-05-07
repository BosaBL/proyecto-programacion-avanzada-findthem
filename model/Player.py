class Player:
    def __init__(self, name: str, points: int):
        self.__name = name
        self.__points = points

    def getName(self):
        return self.__name

    def getPoints(self):
        return self.__points

    def addPoints(self, points: int):
        self.__points += points

    def resetPoints(self):
        self.__points = 0
