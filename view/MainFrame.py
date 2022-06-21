"""
Created on 26-04-2022

@author: alvaro
"""
import wx
from view.GamePanel import GamePanel
from view.Menu import *


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
        self.menuPanel = MenuPanel(self)
        self.menuPanel.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.menuPanel)

        self.SetSizerAndFit(self.sizer)

        self.Show()
        self.Centre()

    def showDifficulty(self):
        self.difficultyPanel = DifficultyPanel(self)
        self.difficultyPanel.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.difficultyPanel)
        self.SetSizerAndFit(self.sizer)

        self.Show()
        self.Centre()

    def startGame(self, config: dict):
        self.gamePanel = GamePanel(self, config)
        self.gamePanel.Show()
        self.sizer.Add(self.gamePanel)
        self.SetSizerAndFit(self.sizer)

        self.Centre()
        self.Show()

    def openScoreboard(self):
        self.scoreboar = ScoreBoard(self)
        self.scoreboar.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.scoreboar)
        self.SetSizerAndFit(self.sizer)

        self.Show()
        self.Centre
