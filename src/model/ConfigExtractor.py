"""
Clase ConfigExtractor
#######################
Extrae la configuración desde un archivo.
"""


import os
import configparser


class ConfigExtractor:
    def __init__(self):
        self.__BASEPATH = os.path.abspath(os.path.dirname("__file__"))

        self.__parser = configparser.ConfigParser()
        self.__parser.read(os.path.join(self.__BASEPATH, "config.cfg"))

    """
    Extrae la configuración para una dificultad específica.

    :return: Diccionario con las llaves como la configuración y valor como el valor.
    :rtype: dict
    """

    def getConfig(self, difficulty):
        return dict(self.__parser[difficulty])
