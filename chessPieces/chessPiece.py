from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QPushButton

class ChessPiece(QPixmap):
    def __init__(self, player : str, r : int, c : int) -> None:
        super().__init__()
        self.player : str = player
        self.row = r
        self.col = c

    def loadImage(self, imageLocation : str) -> None:
        self.load(imageLocation)

    def getMoves(self, curState : list[list]) -> list[list[int]]:
        return []
