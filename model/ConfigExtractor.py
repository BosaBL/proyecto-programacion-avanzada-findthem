import os
import configparser


class ConfigExtractor:
    def __init__(self):
        self.__BASEPATH = os.path.abspath(os.path.dirname("__file__"))

        self.__parser = configparser.ConfigParser()
        self.__parser.read(os.path.join(self.__BASEPATH, "config.cfg"))

    def getConfig(self, difficulty):
        return dict(self.__parser[difficulty])
