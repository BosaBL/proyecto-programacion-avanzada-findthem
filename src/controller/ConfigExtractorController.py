"""
Clase ConfigExtractorController
###############################
Controlador de :py:class:`model.ConfigExtractor`
"""

from model.ConfigExtractor import ConfigExtractor


class ConfigExtractorController:
    def __init__(self):
        self.__configExtractor = ConfigExtractor()

    """
    Devuelve una configuración de una dificultad específica.
    
    :param difficulty: dificultad deseada.
    :type difficulty: "EASY" | "MEDIUM" | "HARD"
    :return: diccionario con las distintas configuraciones.
    :rtype: "EASY" | "MEDIUM" | "HARD"
    """

    def getConfig(self, difficulty):
        return self.__configExtractor.getConfig(difficulty)
