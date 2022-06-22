"""!
Controlador de model.ConfigExtractor
"""

from model.ConfigExtractor import ConfigExtractor


class ConfigExtractorController:
    def __init__(self):
        self.__configExtractor = ConfigExtractor()

    ##
    # @return dict(): diccionario con la configuración de juego.
    def getConfig(self, difficulty):
        return self.__configExtractor.getConfig(difficulty)
