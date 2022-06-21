"""
Created on 30-05-2022

@author: matias
"""
import wx
import wx.grid as wxgrid

from controller.DatabaseController import DatabaseController


class ScoreBoard(wx.Panel):
    def __init__(self, parent):
        self.parent = parent
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)

        wx.Panel.__init__(self, parent, size=(500, 500))
        self.SetBackgroundColour("turquoise")
        self.title = wx.StaticText(
            self, -1, "TABLA DE PUNTAJE", style=wx.ALIGN_CENTER, pos=(130, 50)
        )
        self.count = 18
        self.font = wx.Font(
            self.count, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL
        )
        self.title.SetFont(self.font)
        self.vsizer.Add(self.title, 0, wx.ALL | wx.ALIGN_CENTER, 10)

        self.pointList = PointList(self)
        self.hsizer.Add(self.pointList, wx.ID_ANY, wx.EXPAND | wx.ALL)

        self.vsizer.Add(self.hsizer, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        self.buttonBack = wx.Button(self, label="VOLVER", size=(100, 30))
        self.vsizer.Add(self.buttonBack, 0, wx.ALIGN_CENTER, border=40)
        self.buttonBack.Bind(wx.EVT_BUTTON, self.back)
        self.SetSizer(self.vsizer)
        self.Layout()

    def back(self, evt):
        self.Destroy()
        self.parent.showMenu()


class PointList(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(100, 100))

        self.font = wx.Font(
            13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL
        )

        self.db = DatabaseController()
        self.sortedDb = self.db.descOrder()

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        row = len(self.sortedDb)
        column = 2
        self.grid = wxgrid.Grid(self, -1)

        self.grid.CreateGrid(row, column, wxgrid.Grid.GridSelectNone)
        self.grid.EnableEditing(False)

        self.grid.SetColLabelValue(0, "NOMBRE")
        self.grid.SetColLabelValue(1, "PUNTOS")

        header = ["Player", "Score"]
        width = [100, 100]
        for idx, player in enumerate(self.sortedDb):
            self.grid.SetCellValue(idx, 0, player["Name"])
            self.grid.SetCellValue(idx, 1, player["Points"])
            self.grid.SetCellAlignment(idx, 1, wx.ALIGN_CENTER, wx.ALIGN_CENTRE)
            self.grid.SetCellAlignment(idx, 1, wx.ALIGN_CENTER, wx.ALIGN_CENTRE)
            self.grid.SetCellFont(idx, 0, self.font)
            self.grid.SetCellFont(idx, 1, self.font)

        self.sizer.Add(self.grid, wx.ALL)
        self.SetSizer(self.sizer)
