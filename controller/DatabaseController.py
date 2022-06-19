'''
Created on 08-06-2022

@author: matias
'''
from model.Database import Database

class DatabaseController:
    def databaseConnection(self):
        return Database()