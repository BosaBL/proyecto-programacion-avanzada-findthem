"""
Created on 08-06-2022

@author: matias
"""
from model.Database import Database


class DatabaseController:
    def __init__(self):
        self.__database = Database()

    def databaseConnection(self):
        return self.__database

    def descOrder(self):
        list = self.__database.readScoreBoard()
        list.sort(key=lambda x: int(x["Points"]), reverse=True)
        return list
