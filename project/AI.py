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
            enemyCol='B'
        else:
            myCol='B'
            enemyCol='N'
        moves={}
        real=[]
        moves=[]
        for row_1 in range(8):
            for col_1 in range(8):
                if myCol in board[row_1][col_1]:
                    tempMoves=self.movimientosPosibles(board[row_1][col_1],board,(row_1,col_1))
                    if len(tempMoves)>=1:
                        for pos_1 in tempMoves:
                            value = self.getStateValue(self.getMove(board,(row_1,col_1),pos_1),myCol)
                            moves.append([((row_1,col_1),pos_1),value,[]])
                          
                            
        for move in moves:
            iteration2 = self.getMove(board,move[0][0],move[0][1])
            for row_2 in range(8):
                for col_2 in range(8):
                    if enemyCol in iteration2[row_2][col_2]:
                        tempMoves2=self.movimientosPosibles(iteration2[row_2][col_2],iteration2,(row_2,col_2))
                        if len(tempMoves2)>=1:
                            for pos_2 in tempMoves2:
                                value =self.getStateValue(self.getMove(iteration2,(row_2,col_2),pos_2),myCol)
                                move[2].append([((row_2,col_2),pos_2),value,[]])
                     

        for move in moves:
            value=self.getMinState(move[2])[1]
            move[1]=value
                
        return self.getMaxState(moves)[0]
 

    def getStateValue(self,state,myCol):
        if 'N' in myCol:
            myCol='N'
            enemyCol='B'
        else:
            myCol='B'
            enemyCol='N'       
        res=0
        res+=self.getStateValueAux(state,myCol)
        res-=(self.getStateValueAux(state,enemyCol)/2)          
        return res
    
    def getStateValueAux(self,state,myCol):    
        res=0
        isMyKing =False
        for row in state:
            for col in row:
                if(myCol in col):
                    res+=getPieceValue(col)
                if(col=="NR" and myCol=='N'):
                    isEnemyKing =True
                if(col=="BR" and myCol=='B'):
                    isEnemyKing =True                    
        if(not isMyKing):
            res-=0            
        return res
    
    def getMove(self,board,posIni,posFin):
        tempBoard = copyBoard(board)
        piece = tempBoard[posIni[0]][posIni[1]] 
        tempBoard[posIni[0]][posIni[1]] = ""
        tempBoard[posFin[0]][posFin[1]] = piece
        return tempBoard

        
    def getMaxState(self,states):

        maxState = states[0]
        for state in states:
            if(state[1]>maxState[1]):
                maxState=state
            elif(state[1]==maxState[1]):
                maxState=random.choice([state,maxState])
        return maxState
    
    def getMinState(self,states):
        minState = states[0]
        for state in states:
            if(state[1]<minState[1]):
                minState=state
            elif(state[1]==minState[1]):
                minState=random.choice([state,minState])                
        return minState   

    def getMaxMissedPiece(self,pieces):
        values = []
        for i in range(len(pieces)):
            values.append(getPieceValue(pieces[i]))

        maxInd=values.index(max(values))
        
        return pieces[maxInd]



def copyBoard(board):
    newBoard = []
    for row in board:
        newBoard.append(row[:])
    return newBoard


def printM(matrix):
    for i in matrix:
        for j in i:
            if j=="":
                print("__", end=" ")
            else:
                print(j,end=" ")
        print()
        
def getPieceValue(piece):
    if ('P' in piece):
        return 1
    elif('A' in piece) or ('C' in piece) :
        return 3
    elif('T' in piece):
        return 5
    elif ('D' in piece):
        return 9
    elif ('R' in piece):
        return 300
    else:
        return 0
