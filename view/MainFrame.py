"""
Created on 26-04-2022

@author: alvaro
"""
import wx
from view.GamePanels import GamePanel


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="FindThem")

        self.gamePanel = GamePanel(self, 3, 8)
        self.gamePanel.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.gamePanel, 1, wx.EXPAND | wx.ALL)

        self.SetSizerAndFit(self.sizer)

        self.Layout()

        self.Show()
