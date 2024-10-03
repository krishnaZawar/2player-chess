from header import *
from boardCell import BoardCell
from constants import *

from chessPieces import *

class ChessBoard(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("chess game")
        self.setGeometry(0, 0, 1920, 1080)

        self.initBord()
        self.placePieces()

        self.playerLabel = QLabel(self)
        self.playerLabel.setFont(QFont('calibri', 20))
        self.playerLabel.setGeometry(1000, 100, 200, 30)

        self.curSelection : BoardCell = None
        self.curPlayer : str = 'white'


        self.playerLabel.setText(f"move : {self.curPlayer}")

        self.show()
    
    def initBord(self) -> None:
        self.board = QWidget(self)

        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)

        self.board.setGeometry(100, 40, BOARD_SIZE, BOARD_SIZE)

        # num = 1
        # letters = 'abcdefgh'
        # for letter in letters:
        #     layout.addWidget(QLabel(letter), 0, num, Qt.AlignmentFlag.AlignCenter)
        #     layout.addWidget(QLabel(letter), 9, num, Qt.AlignmentFlag.AlignCenter)
        #     layout.addWidget(QLabel(f"{num}"), num, 0, Qt.AlignmentFlag.AlignCenter)
        #     layout.addWidget(QLabel(f"{num}"), num, 9, Qt.AlignmentFlag.AlignCenter)
        #     num += 1

        color = BLACK
        self.board_layout : list[list[BoardCell]] = []
        for row in range(8):
            self.board_layout.append([i for i in range(8)])
            if row % 2 == 1:
                col = 1
            else:
                col = 8
            while col >= 1 and col <= 8:
                cell = BoardCell(row, col-1, color)
                cell.clicked.connect(lambda checked, this_cell = cell: self.selectCell(this_cell))
                self.board_layout[-1][col-1] = cell
                if color == BLACK:
                    color = WHITE
                else:
                    color = BLACK
                layout.addWidget(cell, row, col)

                if row % 2 == 1:
                    col += 1
                else:
                    col -= 1
            
        self.board.setLayout(layout)
    
    def placePieces(self) -> None:
        # black side
        self.board_layout[0][0].occupyCell(rook.Rook('black', 0, 0))
        self.board_layout[0][1].occupyCell(knight.Knight('black', 0, 1))
        self.board_layout[0][2].occupyCell(camel.Camel('black', 0, 2))
        self.board_layout[0][3].occupyCell(queen.Queen('black', 0, 3))
        self.board_layout[0][4].occupyCell(king.King('black', 0, 4))
        self.board_layout[0][5].occupyCell(camel.Camel('black', 0, 5))
        self.board_layout[0][6].occupyCell(knight.Knight('black', 0, 6))
        self.board_layout[0][7].occupyCell(rook.Rook('black', 0, 7))

        for i in range(8):
            self.board_layout[1][i].occupyCell(pawn.Pawn('black', 1, i))

        # white side
        self.board_layout[7][0].occupyCell(rook.Rook('white', 7, 0))
        self.board_layout[7][1].occupyCell(knight.Knight('white', 7, 1))
        self.board_layout[7][2].occupyCell(camel.Camel('white', 7, 2))
        self.board_layout[7][3].occupyCell(queen.Queen('white', 7, 3))
        self.board_layout[7][4].occupyCell(king.King('white', 7, 4))
        self.board_layout[7][5].occupyCell(camel.Camel('white', 7, 5))
        self.board_layout[7][6].occupyCell(knight.Knight('white', 7, 6))
        self.board_layout[7][7].occupyCell(rook.Rook('white', 7, 7))

        for i in range(8):
            self.board_layout[6][i].occupyCell(pawn.Pawn('white', 6, i))


    def showPossibleMoves(self, show : bool, piece : chessPiece) -> None:
        if not piece:
            return
        if not self.curPlayer == piece.player:
            return
        possibleMoves = piece.getMoves(self.board_layout)

        for move in possibleMoves:
            if show:
                state = 'canGo'
            else:
                state = 'normal'
            self.board_layout[move[0]][move[1]].setState(state)

    def updateBoard(self, newSelection : BoardCell) -> None:
        piece = self.curSelection.piece

        self.showPossibleMoves(False, piece)
        if type(piece) == pawn.Pawn:
            piece.canDoubleJump = False
            if newSelection.row == 0 or newSelection.row == 7:
                piece = queen.Queen(piece.player, piece.row, piece.col)
        
        if newSelection.isOccupied:
            if type(newSelection.piece) == king.King:
                QMessageBox().question(self, "", f'{self.curPlayer} player wins!!', QMessageBox.StandardButton.Ok)
                self.close()
        
        newSelection.occupyCell(piece)
        self.curSelection.emptyCell()

        if self.curPlayer == 'white':
            self.curPlayer = 'black'
        else:
            self.curPlayer = 'white'

        self.playerLabel.setText(f"move : {self.curPlayer}")
        
    def selectCell(self, newSelection : BoardCell) -> None:
        if self.curSelection:
            self.curSelection.setState('normal')
            if self.curSelection == newSelection:
                self.showPossibleMoves(False, self.curSelection.piece)
                self.curSelection = None
                return
            if newSelection.state == 'canGo':
                self.updateBoard(newSelection)
                self.curSelection = None
                return
            self.showPossibleMoves(False, self.curSelection.piece)
            self.curSelection.setState('normal')
        self.curSelection = newSelection
        newSelection.setState('selected')
        self.showPossibleMoves(True, self.curSelection.piece)