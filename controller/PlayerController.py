'''
Created on 13-05-2022

@author: matias
'''
from model.Player import Player
class PlayerController():
    def createPlayer(self, name: str, points: int):
        return (Player(name,points))