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
        self.showMenu()

    def showMenu(self):
        self.menuPanel = MenuPanel(self)
        self.menuPanel.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.menuPanel)

        self.SetSizerAndFit(self.sizer)

        self.Show()
        self.Centre()

    def startEasyGame(self):
        self.gamePanel = GamePanel(self, 3, 6)
        self.gamePanel.Show()
        self.sizer.Add(self.gamePanel)
        self.SetSizerAndFit(self.sizer)

        self.Centre()
        self.Show()
    
    def startMediumGame(self):
        self.gamePanel = GamePanel(self, 4, 7)
        self.gamePanel.Show()
        self.sizer.Add(self.gamePanel)
        self.SetSizerAndFit(self.sizer)

        self.Centre()
        self.Show()
    
    def startHardGame(self):
        self.gamePanel = GamePanel(self, 5, 8)
        self.gamePanel.Show()
        self.sizer.Add(self.gamePanel)
        self.SetSizerAndFit(self.sizer)

        self.Centre()
        self.Show()
