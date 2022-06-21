"""
Clase BoardController
#######################
Controlador de :py:class:`model.Board`
\nse puede interactuar con este objeto como si se tratase de un vector.
"""

from model.Board import Board
from model.Card import Card
from model.CardFinder import CardFinder

import random as rand


class BoardController:
    """
    :param rows: filas del tablero.
    :type rows: int
    :param cols: columnas del tablero.
    :type cols: int
    """

    def __init__(self, rows: int, cols: int):
        self.__rows = rows
        self.__cols = cols

        self.__cardDict = CardFinder().getCardPathIds()

        self.__gameBoard = Board(rows, cols)

    def generateCardList(self):
        """
        :return: lista de cartas.
        :rtype: list[Card]
        """
        cardList = []

        for id, path in self.__cardDict.items():
            cardList.append(Card(id, path))

        return cardList

    def populateGameBoard(self):
        """
        Llena el tablero de carta y las desordena.
        """
        for _ in range((self.__rows * self.__cols) // 2):
            randomCard = rand.choice(self.generateCardList())
            for i in range(2):
                self.__gameBoard.appendItem(randomCard)

        self.__gameBoard.shuffleVector()

    def boardSize(self):
        """
        :return: tamaño del tablero.
        :rtype: tuple(int)
        """
        return (self.__rows, self.__cols)

    def __repr__(self):
        return self.__gameBoard.getBoardMatrix()

    def __setitem__(self, idx, item):
        self.__gameBoard.setItem((((idx[0] * self.__cols)) + idx[1]), item)

    def __getitem__(self, idx):
        return self.__gameBoard.getBoardMatrix()[idx[0]][idx[1]]

    def __str__(self):
        return str(self.__gameBoard.getBoardMatrix())
