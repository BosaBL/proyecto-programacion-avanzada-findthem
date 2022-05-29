"""
Created on 15-05-2022

@author: alvaro
"""
import wx


# class of new window to choose difficulty options
class DifficultyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(500, 500))
        self.parent = parent
        self.title = wx.StaticText(self, -1, "DIFFICULTY", pos=(210, 50))
        self.buttonEasy = wx.Button(self, -1, "EASY", pos=(190, 140), size=(100, 30))
        self.buttonEasy.Bind(wx.EVT_BUTTON, self.easyMode)
        self.buttonMedium = wx.Button(
            self, -1, "MEDIUM", pos=(190, 210), size=(100, 30)
        )
        self.buttonHard = wx.Button(self, -1, "HARD", pos=(190, 280), size=(100, 30))
        self.SetBackgroundColour(wx.Colour(1000, 1000, 1000))
        self.Show(True)
        self.Centre()

    def easyMode(self, evt):
        self.Destroy()
        self.parent.startGame()


# this class creates the window to view the scoreboard
class ScoreBoard(wx.Frame):
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent, title=title, size=(500, 500))
        self.Show(True)
        self.title = wx.StaticText(self, -1, "SCOREBOARD", pos=(210, 50))
        # provisory


# main window creation class to function as menu
class MenuPanel(wx.Panel):
    def __init__(self, parent):
        self.parent = parent
        wx.Panel.__init__(self, parent, size=(500, 500))
        self.buttonStart = wx.Button(
            self, label="START", pos=(190, 140), size=(100, 30)
        )
        self.buttonStart.Bind(wx.EVT_BUTTON, self.difficulty)
        self.panel = wx.Panel(self, -1)
        self.title = wx.StaticText(self, -1, "FIND THEM", pos=(210, 50))
        self.buttonScoreBoard = wx.Button(
            self, -1, "SCOREBOARD", pos=(190, 210), size=(100, 30)
        )
        self.buttonScoreBoard.Bind(wx.EVT_BUTTON, self.scoreboard)
        self.buttonExit = wx.Button(self, -1, "EXIT", pos=(190, 280), size=(100, 30))
        self.buttonExit.Bind(wx.EVT_BUTTON, self.delete)

    def difficulty(self, event):
        self.Destroy()
        self.panel = DifficultyPanel(self.parent)

    def delete(self, event):
        self.parent.Destroy()

    def scoreboard(self, event):
        self.title = "FIND THEM"
        self.frame = ScoreBoard(title=self.title)
