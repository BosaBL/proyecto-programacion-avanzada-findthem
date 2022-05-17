"""
Created on 26-04-2022

@author: alvaro
"""
import wx
from view.GamePanels import GamePanel
from view.Menu import *



class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="FindThem", style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        self.gamePanel =MenuPanel(self)
        self.gamePanel.Show()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.gamePanel)

        self.SetSizerAndFit(self.sizer)

        self.Show()