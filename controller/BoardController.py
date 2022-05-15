from model.Board import Board
from model.Card import Card
from model.CardFinder import CardFinder

import random as rand


class BoardController:
    def __init__(self, rows: int, cols: int):
        self.__rows = rows
        self.__cols = cols

        self.__cardDict = CardFinder().getCardPathIds()

        self.__gameBoard = Board(rows, cols)

    def generateCardList(self):

        cardList = []

        for id, path in self.__cardDict.items():
            cardList.append(Card(id, path))

        return cardList

    def populateGameBoard(self):

        row = 0
        col = 0

        for _ in range((self.__rows * self.__cols) // 2):
            randomCard = rand.choice(self.generateCardList())
            for i in range(2):
                self.__gameBoard.appendItem(randomCard)

        self.__gameBoard.shuffleVector()

    def __repr__(self):
        return self.__gameBoard.getBoardMatrix()

    def __getitem__(self, idx):
        return self.__gameBoard.getBoardMatrix()[idx]

    def __str__(self):
        return str(self.__gameBoard.getBoardMatrix())
