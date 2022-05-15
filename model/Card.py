"""
Created on 03-05-2022

@author: alvar
"""


class Card:
    def __init__(self, identifier: int, path: str):
        self.__id = identifier
        self.__imagePath = path

    def getId(self):
        return self.__id

    def getPath(self):
        return self.__imagePath
