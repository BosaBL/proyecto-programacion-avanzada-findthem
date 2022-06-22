"""!
Clase Menu
Encargada de la interfáz visual del menú.
"""
import wx
from controller.ConfigExtractorController import ConfigExtractorController


# class of new window to choose difficulty options
class DifficultyPanel(wx.Panel):
    ## Interfáz del menú de dificultad.
    # @param parent clase padre.
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(500, 500))

        self.SetBackgroundColour("turquoise")
        self.parent = parent
        self.title = wx.StaticText(self, -1, "DIFICULTAD", pos=(180, 50))
        self.count = 18
        self.font = wx.Font(
            self.count, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL
        )
        self.title.SetFont(self.font)
        self.buttonEasy = wx.Button(self, -1, "FACIL", pos=(190, 140), size=(100, 30))
        self.buttonEasy.Bind(wx.EVT_BUTTON, self.easyMode)
        self.buttonMedium = wx.Button(self, -1, "MEDIO", pos=(190, 210), size=(100, 30))
        self.buttonMedium.Bind(wx.EVT_BUTTON, self.mediumMode)
        self.buttonHard = wx.Button(self, -1, "DIFICIL", pos=(190, 280), size=(100, 30))
        self.buttonHard.Bind(wx.EVT_BUTTON, self.hardMode)

        self.buttonBack = wx.Button(
            self, label="VOLVER", pos=(190, 400), size=(100, 30)
        )
        self.buttonBack.Bind(wx.EVT_BUTTON, self.back)

        self.Show(True)
        self.Centre()

    ## Devuelve al menú anterior
    # @param evt evento
    def back(self, evt):

        self.Destroy()
        self.parent.showMenu()

    ## Comienza el juego en la dificultad FACIL.
    # @param evt evento
    def easyMode(self, evt):
        self.Destroy()
        config = ConfigExtractorController().getConfig("EASY")
        self.parent.startGame(config)

    ## Comienza el juego en la dificultad MEDIA.
    # @param evt evento
    def mediumMode(self, evt):
        self.Destroy()
        config = ConfigExtractorController().getConfig("MEDIUM")
        self.parent.startGame(config)

    ## Comienza el juego en la dificultad DIFICIL.
    # @param evt evento
    def hardMode(self, evt):

        self.Destroy()
        config = ConfigExtractorController().getConfig("HARD")
        self.parent.startGame(config)


# main window creation class to function as menu
class MenuPanel(wx.Panel):

    ## Interfáz del menú principal.
    # @param evt evento
    def __init__(self, parent):
        self.parent = parent
        wx.Panel.__init__(self, parent, size=(500, 500))
        self.SetBackgroundColour("turquoise")
        self.title = wx.StaticText(self, -1, "FIND THEM", pos=(180, 50))
        self.count = 18
        self.font = wx.Font(
            self.count, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL
        )
        self.title.SetFont(self.font)

        self.buttonStart = wx.Button(
            self, label="JUGAR", pos=(190, 140), size=(100, 30)
        )
        self.buttonStart.Bind(wx.EVT_BUTTON, self.difficulty)
        self.panel = wx.Panel(self, -1)
        self.buttonScoreBoard = wx.Button(
            self, -1, "PUNTAJES", pos=(190, 210), size=(100, 30)
        )
        self.buttonScoreBoard.Bind(wx.EVT_BUTTON, self.scoreboard)
        self.buttonExit = wx.Button(self, -1, "SALIR", pos=(190, 280), size=(100, 30))
        self.buttonExit.Bind(wx.EVT_BUTTON, self.delete)

    ## Muestra el menú de dificultad `view.Menu.DifficultyPanel`.
    # @param event evento
    def difficulty(self, event):
        self.Destroy()
        self.panel = DifficultyPanel(self.parent)

    ## Destruye la clase padre.
    # @param event evento
    def delete(self, event):
        self.parent.Destroy()

    ## Muestra el menú de dificultad `view.ScoreBoard`.
    # @param event evento
    def scoreboard(self, evt):
        self.Destroy()
        self.parent.openScoreboard()
