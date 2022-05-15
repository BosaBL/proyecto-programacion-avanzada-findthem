"""
Created on 03-05-2022

@author: alvar
"""


class Menu:
    def __init__(self):
        self.__difficulty = 0

    def setDifficulty(self, n: str):
        self.__difficulty = n

    def getDifficulty(self):
        return self.__difficulty
