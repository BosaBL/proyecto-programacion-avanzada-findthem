"""
Clase PlayerController
#######################
Controlador de la clase :py:class:`model.Player`
"""
from model.Player import Player


class PlayerController:
    def createPlayer(name: str, points: int):
        """
        :return: jugador.
        :rtype: Player
        """
        return Player(name, points)
