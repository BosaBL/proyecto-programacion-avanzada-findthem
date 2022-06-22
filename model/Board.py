"""!
Clase Board
Encargada de la lógica del tablero
"""
from math import fabs
from random import shuffle


class Board:
    ##
    # @param rows int: filas del tablero.
    # @param cols int: columnas del tablero.
    def __init__(self, rows: int, cols: int):
        self.__cols = cols
        self.__rows = rows
        self.__boardVector = []

    ##
    # @return boardMatrix list[int]: version matricial del tablero.
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

    ##
    # @return tuple(row,cols): retorna una tupla con el tamaño de la matríz.
    def getSize(self):
        return (self.__rows, self.__rows)

    ##   Inserta un elemento al final de la matriz.
    # @param item Card: elemento.
    def appendItem(self, item):
        self.__boardVector.append(item)

    ## Inserta un elemento en el índice deseado.
    # @param item int: índice
    # @param item Card: elemento.
    def setItem(self, idx, item):
        self.__boardVector[idx] = item

    ## Desordena la matríz.
    def shuffleVector(self):
        shuffle(self.__boardVector)

    ## Limpia la matriz.
    def clearBoardVector(self):
        self.__boardVector = [None for _ in range(self.__cols * self.__rows)]
