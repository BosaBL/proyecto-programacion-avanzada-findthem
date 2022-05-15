import wx
import wx.grid as gridLib

from controller.BoardController import BoardController


class GamePanel(wx.Panel):
    def __init__(self, parent, rows: int, cols: int):
        wx.Panel.__init__(self, parent=parent)

        self.matrixBoard = BoardController(rows, cols)
        self.matrixBoard.populateGameBoard()

        self.gridBoard = gridLib.Grid(self)
        self.gridBoard.CreateGrid(
            self.matrixBoard.boardSize()[0], self.matrixBoard.boardSize()[1]
        )
        self.gridBoard.SetRowLabelSize(0)
        self.gridBoard.SetColLabelSize(0)

        for i in range(self.matrixBoard.boardSize()[0]):
            for j in range(self.matrixBoard.boardSize()[1]):
                img = wx.Bitmap("img/back.png")
                img = self.scale_bitmap(img, 100, 150)
                imagerender = MyImageRenderer(img)

                self.gridBoard.SetCellRenderer(i, j, imagerender)
                self.gridBoard.SetColSize(i, img.GetHeight() + 2)
                self.gridBoard.SetRowSize(i, img.GetWidth() + 2)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.gridBoard, 1, wx.EXPAND)

        self.SetSizerAndFit(self.sizer)

    def scale_bitmap(self, bitmap, width, height):
        image = wx.Bitmap.ConvertToImage(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result


class MyImageRenderer(wx.grid.GridCellRenderer):
    def __init__(self, img):
        wx.grid.GridCellRenderer.__init__(self)
        self.img = img

    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        image = wx.MemoryDC()
        image.SelectObject(self.img)
        dc.SetBackgroundMode(wx.SOLID)
        if isSelected:
            dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))
        else:
            dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))
        dc.DrawRectangle(rect)
        width, height = self.img.GetWidth(), self.img.GetHeight()
        if width > rect.width - 2:
            width = rect.width - 2
        if height > rect.height - 2:
            height = rect.height - 2
        dc.Blit(rect.x + 1, rect.y + 1, width, height, image, 0, 0, wx.COPY, True)
