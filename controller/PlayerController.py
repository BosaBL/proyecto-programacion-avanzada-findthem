"""!
Controlador de model.Player
"""
from model.Player import Player


class PlayerController:
    ## @param name str: nombre.
    # @param points int: puntaje
    # @returns Player: retorna un Player
    def createPlayer(name: str, points: int):
        return Player(name, points)
