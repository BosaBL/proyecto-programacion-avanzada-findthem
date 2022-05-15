from random import shuffle


class Board:
    def __init__(self, rows: int, cols: int):
        self.__cols = cols
        self.__rows = rows
        self.__boardMatrix = [[None for _ in range(cols)] for _ in range(rows)]

    def getBoardMatrix(self):
        return self.__boardMatrix

    def getSize(self):
        return (self.__rows, self.__rows)

    def setCell(self, row: int, col: int, value):
        self.__boardMatrix[row][col] = value

    def shuffleMatrix(self):
        shuffle(self.__boardMatrix)

    def clearBoardMatrix(self):
        self.__boardMatrix = [
            [None for _ in range(self.__cols)] for _ in range(self.__rows)
        ]
