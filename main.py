import sys

from board import ChessBoard
from header import QApplication

def main() -> None:
    app = QApplication(sys.argv)

    board = ChessBoard()

    app.exec()

if __name__ == '__main__':
    main()