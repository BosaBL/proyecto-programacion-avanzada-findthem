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

        self.menuPanel = MenuPanel(self)
        self.menuPanel.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.menuPanel)

        self.SetSizerAndFit(self.sizer)

        self.Show()

    def startGame(self):
        self.menuPanel.Destroy()

        self.gamePanel = GamePanel(self, 3, 6)
        self.gamePanel.Show()
        self.sizer.Add(self.gamePanel)
        self.SetSizerAndFit(self.sizer)

        self.Centre()
        self.Show()
