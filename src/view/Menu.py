"""
Clase Menu
#################
Encargada de la lógca del menú principal y de dificultad
"""
import wx
from controller.ConfigExtractorController import ConfigExtractorController


# class of new window to choose difficulty options
class DifficultyPanel(wx.Panel):
    """
    Panel de dificultades

    :param parent: clase padre.
    """

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

    def back(self, evt):
        """
        Devuelve al menú anterior

        :param evt: evento.
        :type evt: wx.Evt
        """
        self.Destroy()
        self.parent.showMenu()

    def easyMode(self, evt):
        """
        Comienza un juego en modo fácil.

        :param evt: evento.
        :type evt: wx.EVT
        """
        self.Destroy()
        config = ConfigExtractorController().getConfig("EASY")
        self.parent.startGame(config)

    def mediumMode(self, evt):
        """
        Comienza un juego en modo medio.

        :param evt: evento.
        :type evt: wx.EVT
        """
        self.Destroy()
        config = ConfigExtractorController().getConfig("MEDIUM")
        self.parent.startGame(config)

    def hardMode(self, evt):
        """
        Comienza un juego en modo dificil.

        :param evt: evento.
        :type evt: wx.EVT
        """
        self.Destroy()
        config = ConfigExtractorController().getConfig("HARD")
        self.parent.startGame(config)


# main window creation class to function as menu
class MenuPanel(wx.Panel):
    """
    Panel de menú principal

    :param parent: clase padre.
    """

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

    def difficulty(self, event):
        """
        Muestra el panel de dificultades :py:class:`view.Menu.DifficultyPanel`

        :param event: evento.
        :type event: wx.EVT
        """
        self.Destroy()
        self.panel = DifficultyPanel(self.parent)

    def delete(self, event):
        """
        Destruye su Clase Padre.

        :param event: evento.
        :type event: wx.EVT
        """
        self.parent.Destroy()

    def scoreboard(self, evt):
        """
        Muestra el panel de dificultades :py:class:`view.ScoreBoard`

        :param evt: evento.
        :type evt: wx.EVT
        """
        self.Destroy()
        self.parent.openScoreboard()
