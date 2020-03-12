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
                j = j + 1
            i = i + 1
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
                    if len(tempMoves)>1:
                        moves[(row,col)]=AI.movimientosPosibles(self,board[row][col],board,(row,col))
                    
        
        posPiece = random.choice(list(moves.keys()))
        return(posPiece,random.choice(moves[posPiece]))
