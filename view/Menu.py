"""
Created on 15-05-2022

@author: alvaro
"""
import wx
from controller.ConfigExtractorController import ConfigExtractorController


# class of new window to choose difficulty options
class DifficultyPanel(wx.Panel):
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
        self.Destroy()
        self.parent.showMenu()

    def easyMode(self, evt):
        self.Destroy()
        config = ConfigExtractorController().getConfig("EASY")
        self.parent.startGame(config)

    def mediumMode(self, evt):
        self.Destroy()
        config = ConfigExtractorController().getConfig("MEDIUM")
        self.parent.startGame(config)

    def hardMode(self, evt):
        self.Destroy()
        config = ConfigExtractorController().getConfig("HARD")
        self.parent.startGame(config)


# this class creates the window to view the scoreboard
class ScoreBoard(wx.Panel):
    def __init__(self, parent):
        self.parent = parent
        wx.Panel.__init__(self, parent, size=(500, 500))
        self.SetBackgroundColour("turquoise")
        self.title = wx.StaticText(self, -1, "TABLA DE PUNTAJE", pos=(130, 50))
        self.count = 18
        self.font = wx.Font(
            self.count, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL
        )
        self.title.SetFont(self.font)

        self.buttonBack = wx.Button(
            self, label="VOLVER", pos=(190, 450), size=(100, 30)
        )
        self.buttonBack.Bind(wx.EVT_BUTTON, self.back)

    def back(self, evt):
        self.Destroy()
        self.parent.showMenu()

        # provisory


# main window creation class to function as menu
class MenuPanel(wx.Panel):
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
        self.Destroy()
        self.panel = DifficultyPanel(self.parent)

    def delete(self, event):
        self.parent.Destroy()

    def scoreboard(self, evt):
        self.Destroy()
        self.parent.openScoreboard()
