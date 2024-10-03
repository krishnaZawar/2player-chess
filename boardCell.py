from header import QPushButton, QIcon, QSize
from chessPieces.chessPiece import ChessPiece
from constants import *

class BoardCell(QPushButton):
    def __init__(self, r : int, c : int, originalColor : str) -> None:
        super().__init__()

        self.setFixedSize(CELL_SIZE, CELL_SIZE)

        self.original_color = originalColor

        self.row = r
        self.col = c

        self.isOccupied : bool = False
        self.piece : ChessPiece = None

        self.setContentsMargins(0, 0, 0, 0)

        self.setIconSize(QSize(30, 30))

        self.setState('normal')

    def occupyCell(self, piece : ChessPiece) -> None:
            self.isOccupied = True
            self.piece = piece
            piece.row, piece.col = self.row, self.col
            self.setIcon(QIcon(piece))
            self.setState('normal')
    def emptyCell(self) -> None:
            self.isOccupied = False
            self.piece = None
            self.setIcon(QIcon())
            self.setState('normal')

    def setState(self, state : str) -> None:
        '''
        three states:
            selected, normal, canGo
        '''
        self.state = state
        if state == 'normal':
            new_color = self.original_color
        elif state == 'canGo':
            new_color = CAN_GO
        else:
            new_color = SELECTED
        
        self.setStyleSheet(f'background-color : {new_color}')

