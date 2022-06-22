"""!
Clase ConfigExtractor
Extrae la configuración de un archivo .cfg
"""
import os
import configparser


class ConfigExtractor:
    def __init__(self):
        self.__BASEPATH = os.path.abspath(os.path.dirname("__file__"))

        self.__parser = configparser.ConfigParser()
        self.__parser.read(os.path.join(self.__BASEPATH, "config.cfg"))

    ##
    # @param difficulty EASY | MEDIUM | HARD: dificultad.
    # @retun dict(): retorna un diccionario con las configuraciones.
    def getConfig(self, difficulty):
        return dict(self.__parser[difficulty])
