from chessPieces.chessPiece import ChessPiece
from chessPieces.king import King

class Rook(ChessPiece):
    def __init__(self, player : str, r : int, c : int) -> None:
        super().__init__(player, r, c)

        if player == 'white':
            self.loadImage('./images/whiteRook.png')
        else:
            self.loadImage('./images/blackRook.png')

    def getMoves(self, curState : list[list]) -> list[list[int]]:
        possibleMoves : list[list[int]] = []

        row = self.row
        col = self.col
        
        while row+1 < 8:
            if not curState[row+1][col].isOccupied:
                possibleMoves.append([row+1, col])
                row += 1
            else:
                if not curState[row+1][col].piece.player == self.player:
                    possibleMoves.append([row+1, col])
                break

        row = self.row
        col = self.col

        while row-1 >= 0:
            if not curState[row-1][col].isOccupied:
                possibleMoves.append([row-1, col])
                row -= 1
            else:
                if not curState[row-1][col].piece.player == self.player:
                    possibleMoves.append([row-1, col])
                break

        row = self.row
        col = self.col

        while col+1 < 8:
            if not curState[row][col+1].isOccupied:
                possibleMoves.append([row, col+1])
                col += 1
            else:
                if not curState[row][col+1].piece.player == self.player:
                    possibleMoves.append([row, col+1])
                break
        
        row = self.row
        col = self.col

        while col-1 >= 0:
            if not curState[row][col-1].isOccupied:
                possibleMoves.append([row, col-1])
                col -= 1
            else:
                if not curState[row][col-1].piece.player == self.player:
                    possibleMoves.append([row-1, col-1])
                break

        return possibleMoves
    
    def givesCheck(self, curState : list[list]) -> bool:
        row = self.row
        col = self.col

        while row+1 < 8:
            if curState[row+1][col].isOccupied:
                if type(curState[row+1][col].piece) == King and not curState[row+1][col].piece.player == self.player:
                    return True
                break
            row += 1

        row = self.row
        col = self.col

        while row-1 >= 0:
            if  curState[row-1][col].isOccupied:
                if type(curState[row-1][col].piece) == King and not curState[row-1][col].piece.player == self.player:
                    return True
                break
            row -= 1

        row = self.row
        col = self.col

        while col+1 < 8:
            if curState[row][col+1].isOccupied:
                if type(curState[row][col+1].piece) == King and not curState[row][col+1].piece.player == self.player:
                    return True
                break
            col += 1
        
        row = self.row
        col = self.col

        while col-1 >= 0:
            if curState[row][col-1].isOccupied:
                if type(curState[row][col-1].piece) == King and not curState[row][col-1].piece.player == self.player:
                    return True
                break
            col -= 1
        return False
