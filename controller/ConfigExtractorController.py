from model.ConfigExtractor import ConfigExtractor


class ConfigExtractorController:
    def __init__(self):
        self.__configExtractor = ConfigExtractor()

    def getConfig(self, difficulty):
        return self.__configExtractor.getConfig(difficulty)
