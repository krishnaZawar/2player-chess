from chessPieces.chessPiece import *
from chessPieces.king import King

class Pawn(ChessPiece):
    def __init__(self, player : str, r : int, c : int) -> None:
        super().__init__(player, r, c)

        self.canDoubleJump = True

        if player == 'white':
            self.loadImage('./images/whitePawn.png')
        else:
            self.loadImage('./images/blackPawn.png')

    def getMoves(self, curState : list[list]) -> list[list[int]]:
        possibleMoves : list[list[int]] = []

        row = self.row
        col = self.col

        if self.player == 'black':
            if row + 1 < 8 and not curState[row+1][col].isOccupied:
                possibleMoves.append([row+1, col])
                if row + 2 < 8 and not curState[row+2][col].isOccupied and self.canDoubleJump:
                    possibleMoves.append([row+2, col])                    
            if row+1 < 8 and col+1 < 8:
                if curState[row+1][col+1].isOccupied and not curState[row+1][col+1].piece.player == self.player:
                    possibleMoves.append([row+1, col+1])
            if row+1 < 8 and col-1 >= 0:
                if curState[row+1][col-1].isOccupied and not curState[row+1][col-1].piece.player == self.player:
                    possibleMoves.append([row+1, col-1])
        
        if self.player == 'white':
            if row - 1 >= 0 and not curState[row-1][col].isOccupied:
                possibleMoves.append([row-1, col])
                if row - 2 >= 0 and not curState[row-2][col].isOccupied and self.canDoubleJump:
                    possibleMoves.append([row-2, col])
            if row-1 >= 0 and col+1 < 8:
                if curState[row-1][col+1].isOccupied and not curState[row-1][col+1].piece.player == self.player:
                    possibleMoves.append([row-1, col+1])
            if row-1 >= 0 and col-1 >= 0:
                if curState[row-1][col-1].isOccupied and not curState[row-1][col-1].piece.player == self.player:
                    possibleMoves.append([row-1, col-1])

        return possibleMoves
    
    def givesCheck(self, curState : list[list]) -> bool:
        row = self.row
        col = self.col

        if self.player == 'black':
            if row+1 < 8 and col+1 < 8:
                if curState[row+1][col+1].isOccupied: 
                    if not curState[row+1][col+1].piece.player == self.player and type(curState[row+1][col+1].piece) == King:
                        return True
            if row+1 < 8 and col-1 >= 0:
                if curState[row+1][col-1].isOccupied:
                    if not curState[row+1][col-1].piece.player == self.player and type(curState[row+1][col-1].piece) == King:
                        return True
        
        if self.player == 'white':
            if row-1 >= 0 and col+1 < 8:
                if curState[row-1][col+1].isOccupied:
                    if not curState[row-1][col+1].piece.player == self.player and type(curState[row-1][col+1]) == King:
                        return True
            if row-1 >= 0 and col-1 >= 0:
                if curState[row-1][col-1].isOccupied:
                    if not curState[row-1][col-1].piece.player == self.player and type(curState[row-1][col-1]) == King:
                        return True
        
        return False