"""
Clase MainFrame
#######################
Encargada de mostrar las distintas interfaces del proyecto.
"""
import wx
from view.GamePanel import GamePanel
from view.Menu import *
from view.ScoreBoard import *


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(
            self,
            None,
            title="FindThem",
            style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER,
        )
        icon = wx.Icon(
            "img/lupa.png",
            wx.BITMAP_TYPE_ANY,
        )
        self.SetIcon(icon)

        self.showMenu()

    def showMenu(self):
        """
        Muestra el menú :py:class:`view.Menu.MenuPanel`.
        """
        self.menuPanel = MenuPanel(self)
        self.menuPanel.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.menuPanel)

        self.SetSizerAndFit(self.sizer)

        self.Show()
        self.Centre()

    def showDifficulty(self):
        """
        Muestra el menú de dificultades :py:class:`view.Menu.MenuPanel`.
        """
        self.difficultyPanel = DifficultyPanel(self)
        self.difficultyPanel.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.difficultyPanel)
        self.SetSizerAndFit(self.sizer)

        self.Show()
        self.Centre()

    def startGame(self, config: dict):
        """
        Muestra y comienza el juego :py:class:`view.GamePanel`.

        :param config: diccionario con las configuraciones de juego.
        :param type: dict
        """
        self.gamePanel = GamePanel(self, config)
        self.gamePanel.Show()
        self.sizer.Add(self.gamePanel)
        self.SetSizerAndFit(self.sizer)

        self.Centre()
        self.Show()

    def openScoreboard(self):
        """
        Muestra el menú de puntajes :py:class:`view.ScoreBoard`.
        """
        self.scoreboar = ScoreBoard(self)
        self.scoreboar.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.scoreboar)
        self.SetSizerAndFit(self.sizer)

        self.Show()
        self.Centre
