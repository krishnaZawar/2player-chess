from chessPieces.chessPiece import ChessPiece

class King(ChessPiece):
    def __init__(self, player : str, r : int, c : int) -> None:
        super().__init__(player, r, c)

        if player == 'white':
            self.loadImage('./images/whiteKing.png')
        else:
            self.loadImage('./images/blackKing.png')
    
    def getMoves(self, curState : list[list]) -> list[list[int]]:
        possibleMoves : list[list[int]] = []

        row = self.row
        col = self.col

        moves_row = [1, -1, 0, 0]
        moves_col = [0, 0, 1, -1]
        
        for i in range(len(moves_row)):
            newRow = self.row + moves_row[i]
            newCol = self.col + moves_col[i]

            if newRow >= 0 and newRow < 8  and newCol >= 0 and newCol < 8:
                if curState[newRow][newCol].isOccupied:
                    if not curState[newRow][newCol].piece.player == self.player:
                        possibleMoves.append([newRow, newCol])
                else:
                    possibleMoves.append([newRow, newCol])
        
        return possibleMoves
    
    def givesCheck(self, curState : list[list]) -> bool:
        row = self.row
        col = self.col

        moves_row = [1, -1, 0, 0]
        moves_col = [0, 0, 1, -1]
        
        for i in range(len(moves_row)):
            newRow = self.row + moves_row[i]
            newCol = self.col + moves_col[i]

            if newRow >= 0 and newRow < 8  and newCol >= 0 and newCol < 8:
                if curState[newRow][newCol].isOccupied:
                    if type(curState[newRow][newCol].piece) == King and not curState[newRow][newCol].piece.player == self.player:
                        return True
        
        return False

        