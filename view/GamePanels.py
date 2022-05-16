import wx
import wx.grid as gridLib

from controller.BoardController import BoardController


class GamePanel(wx.Panel):
    def __init__(self, parent, rows: int, cols: int):
        wx.Panel.__init__(self, parent=parent)

        self.cardTimer = wx.Timer()

        self.__pickedCards = []
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

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.gridBoard, 1, wx.EXPAND)

        self.SetSizerAndFit(self.sizer)

        self.gridBoard.Bind(gridLib.EVT_GRID_CELL_LEFT_CLICK, self._onClick)

    def _onClick(self, event):
        cardPos = (int(event.GetRow()), int(event.GetCol()))

        if not self.matrixBoard[cardPos] or cardPos in self.__pickedCards:
            return

        self.__pickedCards.append(cardPos)

        imgPath = self.matrixBoard[cardPos].getPath()
        imgs = wx.Bitmap(imgPath, wx.BITMAP_TYPE_ANY)
        imgs = self.scaleBitmap(imgs, 100, 150)
        imagerenderers = MyImageRenderer(imgs)
        self.gridBoard.SetCellRenderer(int(cardPos[0]), int(cardPos[1]), imagerenderers)

        if len(self.__pickedCards) == 2:
            print(self.__pickedCards)
            aux = self.__pickedCards
            card = self.matrixBoard[aux[0]].getId()
            nextCard = self.matrixBoard[aux[1]].getId()

            if card == nextCard:
                self.matrixBoard[aux[0]] = None
                self.matrixBoard[aux[1]] = None
            else:
                wx.CallLater(250, self.turnBack)
            self.__pickedCards = []

        self.gridBoard.ClearGrid()

    def turnBack(self):

        for i in range(self.matrixBoard.boardSize()[0]):
            for j in range(self.matrixBoard.boardSize()[1]):
                if self.matrixBoard[(i, j)]:
                    self.img = self.scaleBitmap(self.BACKCARD, 100, 150)
                    self.imagerender = MyImageRenderer(self.img)

                    self.gridBoard.SetCellRenderer(i, j, self.imagerender)
                    self.gridBoard.SetColSize(j, self.img.GetWidth() + 5)
                    self.gridBoard.SetRowSize(i, self.img.GetHeight() + 5)
        self.gridBoard.ClearGrid()

    def scaleBitmap(self, bitmap, width, height):
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
