import posixpath
import wx
from wx.core import EVT_BUTTON, HORIZONTAL
import wx.grid as gridLib

from controller.BoardController import BoardController


class GamePanel(wx.Panel):
    def __init__(self, parent, rows: int, cols: int):
        wx.Panel.__init__(self, parent=parent)

        self.foundPair = 0
        self.time = 60
        self.points = 0
        self.parent = parent

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.gameTimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.timeCounter, self.gameTimer)

        self.pickedFlag = False
        self.pickedCards = []
        self.BACKCARD = wx.Bitmap("img/back.png")

        self.matrixBoard = BoardController(rows, cols)
        self.matrixBoard.populateGameBoard()

        self.gridBoard = gridLib.Grid(self)
        self.gridBoard.CreateGrid(
            self.matrixBoard.boardSize()[0],
            self.matrixBoard.boardSize()[1],
            gridLib.Grid.GridSelectNone,
        )
        self.gridBoard.SetDefaultCellBackgroundColour(
            self.gridBoard.GetLabelBackgroundColour()
        )
        self.gridBoard.SetRowLabelSize(0)
        self.gridBoard.SetColLabelSize(0)
        self.gridBoard.EnableEditing(False)
        self.gridBoard.EnableDragColSize(False)
        self.gridBoard.EnableDragRowSize(False)
        self.gridBoard.SetCellHighlightPenWidth(0)

        self.turnBack()

        self.sizer.Add(self.gridBoard, 1, wx.EXPAND)

        self.gridBoard.Bind(gridLib.EVT_GRID_CELL_LEFT_CLICK, self._onClick)

        self.DataGridSizer = wx.GridBagSizer(15, 15)

        self.TimeLabel = wx.StaticText(self, label="TIEMPO RESTANTE")
        self.TimeLabelCounter = wx.StaticText(self)

        self.DataGridSizer.Add(self.TimeLabel, flag=wx.ALIGN_CENTRE, pos=(0, 0))
        self.DataGridSizer.Add(
            self.TimeLabelCounter, flag=wx.ALIGN_CENTER_HORIZONTAL, pos=(1, 0)
        )

        self.pointLabel = wx.StaticText(self, label="PUNTOS")
        self.pointLabelCounter = wx.StaticText(self, label=f"{self.points}")

        self.DataGridSizer.Add(self.pointLabel, flag=wx.ALIGN_CENTRE, pos=(0, 1))
        self.DataGridSizer.Add(
            self.pointLabelCounter, flag=wx.ALIGN_CENTER_HORIZONTAL, pos=(1, 1)
        )

        self.exitButton = wx.Button(self, label="SALIR")
        self.exitButton.Bind(wx.EVT_BUTTON, self._onLeaveClick)
        self.DataGridSizer.Add(
            self.exitButton, flag=wx.ALIGN_CENTER_HORIZONTAL, pos=(0, 2)
        )

        self.DataGridSizer.AddGrowableCol(1)
        self.DataGridSizer.AddGrowableCol(2)
        self.DataGridSizer.AddGrowableCol(0)

        self.sizer.Add(self.DataGridSizer, 0, wx.EXPAND | wx.ALL, 30)

        self.SetSizerAndFit(self.sizer)
        self.gameTimer.Start(1000)

    def _onClick(self, event):
        cardPos = (int(event.GetRow()), int(event.GetCol()))

        if (
            not self.matrixBoard[cardPos]
            or cardPos in self.pickedCards
            or self.pickedFlag
        ):
            return

        self.pickedCards.append(cardPos)

        imgPath = self.matrixBoard[cardPos].getPath()
        imgs = wx.Bitmap(imgPath, wx.BITMAP_TYPE_ANY)
        imgs = self.scaleBitmap(imgs, 75, 125)
        imagerenderers = MyImageRenderer(imgs)
        self.gridBoard.SetCellRenderer(int(cardPos[0]), int(cardPos[1]), imagerenderers)

        if len(self.pickedCards) == 2:
            aux = self.pickedCards
            card = self.matrixBoard[aux[0]].getId()
            nextCard = self.matrixBoard[aux[1]].getId()

            if card == nextCard:
                self.points += 2
                self.foundPair += 1
                size = self.matrixBoard.boardSize()[0] * self.matrixBoard.boardSize()[1]
                if self.foundPair == size / 2:
                    self.gameTimer.Stop()
                    wx.CallLater(25, self.endGame)
                self.pointLabelCounter.SetLabel(f"{self.points}")
                self.matrixBoard[aux[0]] = None
                self.matrixBoard[aux[1]] = None
            else:
                self.pickedFlag = True
                wx.CallLater(250, self.turnBack)
            self.pickedCards = []

        self.gridBoard.ClearGrid()

    def turnBack(self):
        for i in range(self.matrixBoard.boardSize()[0]):
            for j in range(self.matrixBoard.boardSize()[1]):
                if self.matrixBoard[(i, j)]:
                    self.img = self.scaleBitmap(self.BACKCARD, 75, 125)
                    self.imagerender = MyImageRenderer(self.img)

                    self.gridBoard.SetCellRenderer(i, j, self.imagerender)
                    self.gridBoard.SetColSize(j, self.img.GetWidth() + 5)
                    self.gridBoard.SetRowSize(i, self.img.GetHeight() + 5)
        self.pickedFlag = False
        self.gridBoard.ClearGrid()

    def scaleBitmap(self, bitmap, width, height):
        image = wx.Bitmap.ConvertToImage(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

    def timeCounter(self, e):
        minutes = self.time // 60
        seconds = self.time - minutes * 60

        self.time -= 1
        self.TimeLabelCounter.SetLabel(f"{minutes}:{seconds}")

        if self.time <= 0:
            self.endGame()

    def endGame(self):
        self.points += self.time * 2
        self.pointLabelCounter.SetLabel(f"{self.points}")
        dialog = wx.MessageDialog(
            self,
            "JUEGO TERMINADO",
            caption="JUEGO TERMINADO",
            style=wx.OK,
        )
        dialog.ShowModal()
        dialog.Destroy()

    def _onLeaveClick(self, e):

        dialog = wx.MessageDialog(
            self,
            "¿Estás seguro de que deseas salir?",
            caption="SALIR",
            style=wx.YES_NO,
        )

        if dialog.ShowModal() == wx.ID_YES:
            self.parent.Destroy()
        dialog.Destroy()


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
