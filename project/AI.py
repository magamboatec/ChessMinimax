from Rules import Rules
import random

class AI:
    def movimientosPosibles(self,piece,piecesMatrix,Pos):
        movimientos = []
        rules = Rules()
        for i in range(8):
            for j in range(8):
                if(rules.IsLegalMove(piece,piecesMatrix,(Pos[0],Pos[1]),(i,j))==True):
                    movimientos.append((i,j))
        return movimientos

    def play(self,board,color):
        if 'N' in color:
            myCol='N'
        else:
            myCol='B'
        moves={}
        for row in range(8):
            for col in range(8):
                if myCol in board[row][col]:
                    tempMoves=AI.movimientosPosibles(self,board[row][col],board,(row,col))
                    if len(tempMoves)>=1:
                        moves[(row,col)]=AI.movimientosPosibles(self,board[row][col],board,(row,col))
                    
        
        posPiece = random.choice(list(moves.keys()))
        return(posPiece,random.choice(moves[posPiece]))
    
    def getPieceValue(self,piece):
        if ('P' in piece):
            return 1
        elif('A' in piece) or ('C' in piece) :
            return 3
        elif('T' in piece):
            return 5
        elif ('D' in piece):
            return 9
        elif ('R' in piece):
            return 30
        else:
            return 0    

    def getMaxMissedPiece(self,pieces):
        values = []
        for i in range(len(pieces)):
            values.append(self.getPieceValue(pieces[i]))

        maxInd=values.index(max(values))
        
        return pieces[maxInd]
