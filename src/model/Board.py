"""
Clase Board
#####################
Modelo de un tablero de juego.
"""


from math import fabs
from random import shuffle


class Board:

    """
    :param rows: cantidad de filas
    :param cols: cantidad de columnas
    :type rows: int
    :type cols: int
    """

    def __init__(self, rows: int, cols: int):
        self.__cols = cols
        self.__rows = rows
        self.__boardVector = []

    def getBoardMatrix(self):
        """
        :return: versión matricial del vector.
        :rtype: list[int]
        """
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
        """
        :return: tupla con el tamaño de la matríz.
        :rtype: tuple(int)
        """
        return (self.__rows, self.__cols)

    def appendItem(self, item):
        """
        Añade un elemento al final del vector base.

        :param item: elemento a añadir.
        :type item: Card
        """
        self.__boardVector.append(item)

    def setItem(self, idx, item):
        """
        Modifica un elemento del del vector base.

        :param idx: índice del elemento.
        :type idx: int
        :param item: elemento a añadir.
        :type item: Card
        """
        self.__boardVector[idx] = item

    def shuffleVector(self):
        """
        Desordena el vector base.
        """
        shuffle(self.__boardVector)

    def clearBoardVector(self):
        """
        Vacia el vector base.
        """
        self.__boardVector = [None for _ in range(self.__cols * self.__rows)]
