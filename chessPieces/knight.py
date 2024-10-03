from chessPieces.chessPiece import ChessPiece
from chessPieces.king import King

class Knight(ChessPiece):
    def __init__(self, player : str, r : int, c : int) -> None:
        super().__init__(player, r, c)

        if player == 'white':
            self.loadImage('./images/whiteKnight.png')
        else:
            self.loadImage('./images/blackKnight.png')

    def getMoves(self, curState : list[list]) -> list[list[int]]:
        possibleMoves : list[list[int]] = []

        row = self.row
        col = self.col

        moves_row = [2, 2, -2, -2, 1, 1, -1, -1]
        moves_col = [1, -1, 1, -1, 2, -2, 2, -2]

        for i in range(len(moves_row)):
            newRow = moves_row[i] + row
            newCol = moves_col[i] + col

            if newRow >= 0 and newRow < 8 and newCol >= 0 and newCol < 8:
                if curState[newRow][newCol].isOccupied:
                    if not curState[newRow][newCol].piece.player == self.player:
                        possibleMoves.append([newRow, newCol])
                else:
                    possibleMoves.append([newRow, newCol])

        return possibleMoves
    
    def givesCheck(self, curState : list[list]) -> bool:
        row = self.row
        col = self.col

        moves_row = [2, 2, -2, -2, 1, 1, -1, -1]
        moves_col = [1, -1, 1, -1, 2, -2, 2, -2]

        for i in range(len(moves_row)):
            newRow = moves_row[i] + row
            newCol = moves_col[i] + col

            if newRow >= 0 and newRow < 8 and newCol >= 0 and newCol < 8:
                if curState[newRow][newCol].isOccupied:
                    if type(curState[newRow][newCol].piece) == King and not curState[newRow][newCol].piece.player == self.player:
                        return True
        return False