'''
Created on 30-05-2022

@author: matias
'''
import wx
import wx.grid as wxgrid

class ScoreBoard(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(800,800))

        row = 100
        column = 2
        self.grid = wxgrid.Grid(self, -1)
        self.grid.CreateGrid(row,column)
        self.grid.EnableEditing(False)
        
        header = ["Player", "Score"]
        width = [100, 100]
        for n,col in enumerate(range(column)):
            self.grid.SetColLabelValue(col,header[n])
            self.grid.SetColSize(col,width[n])
        
        self.Centre(True)
        self.Show()
             
app = wx.App()
frame = ScoreBoard(None,"ScoreBoard")
app.MainLoop()