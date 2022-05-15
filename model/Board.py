from math import fabs
from random import shuffle


class Board:
    def __init__(self, rows: int, cols: int):
        self.__cols = cols
        self.__rows = rows
        self.__boardVector = []

    def getBoardMatrix(self):
        boardMatrix = [[None for _ in range(self.__cols)] for _ in range(self.__rows)]
        row = 0
        col = 0

        for i in range(0, len(self.__boardVector)):
            boardMatrix[row][col] = self.__boardVector[i]
            col += 1
            if col == self.__cols:
                row += 1
                col = 0

        return boardMatrix

    def getSize(self):
        return (self.__rows, self.__rows)

    def appendItem(self, item):
        self.__boardVector.append(item)

    def setItem(self, idx, item):
        self.__boardVector[idx] = item

    def shuffleVector(self):
        shuffle(self.__boardVector)

    def clearBoardVector(self):
        self.__boardVector = [None for _ in range(self.__cols * self.__rows)]
