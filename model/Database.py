"""!
Clase Database
Encargada de leer y escribir en la "base de datos" scores.csv
"""
import csv
import os


class Database:
    def __init__(self):
        self.__BASEPATH = os.path.abspath(os.path.dirname("__file__"))
        self.__fields = ["Name", "Points"]

    ## Añade un jugador a la base de datos
    # @param player Player: jugador.
    def addPlayerToScoreBoard(self, player):
        with open(f"{self.__BASEPATH}/scores.csv", "a", newline="") as database:
            csv_writer = csv.DictWriter(database, fieldnames=self.__fields)
            csv_writer.writerow(
                {"Name": player.getName(), "Points": player.getPoints()}
            )

    ##
    # @returns list[players]: lista de jugadores.
    def readScoreBoard(self):
        with open(f"{self.__BASEPATH}/scores.csv", "r") as database:
            players = []
            csv_reader = csv.DictReader(database, fieldnames=self.__fields)
            for row in csv_reader:
                players.append(row)
            return players
