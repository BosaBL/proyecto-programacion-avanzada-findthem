class Board:
    def __init__(self, rows: int, cols: int):
        self.__cols = cols
        self.__rows = rows
        self.__boardMatrix = [[None for _ in range(cols)] for _ in range(rows)]

    def getBoardMatrix(self):
        return self.__boardMatrix

    def setCell(self, row: int, col: int, value):
        self.__boardMatrix[row][col] = value

    def clearBoardMatrix(self):
        self.__boardMatrix = [
            [None for _ in range(self.__cols)] for _ in range(self.__rows)
        ]
