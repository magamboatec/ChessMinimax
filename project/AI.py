from Rules import Rules
import random
from math import inf

class AI:
    def __init__(self):
        self.rules = Rules()
    def movimientosPosibles(self,piece,board,Pos,myCol,isTerminal):
        moves = []
        for i in range(8):
            for j in range(8):
                if(self.rules.IsLegalMove(piece,board,(Pos[0],Pos[1]),(i,j))):
                    if (isTerminal):
                        value = self.getStateValue(self.getMove(board,(Pos[0],Pos[1]),(i,j)),myCol)
                    else:
                        value=0
                    moves.append([((Pos[0],Pos[1]),(i,j)),value,[]])                    
        return moves

    
    def minimax(self,state,depth,playerMove,color):
        if not playerMove:
            best = [(), (), -inf]
        else:
            best = [(), (), +inf]

        if depth == 0:
            value = self.getStateValue(state,"Negro")
            return [(), (), value]
        stateCopy=copyBoard(state)
        for row in range(8):
            for col in range(8):
                if color[0] in state[row][col]:
                    for move in self.rules.GetListOfValidMoves(state,color,(row,col)):
                        x, y = move[0], move[1]
                        stateCopy[x][y] = stateCopy[row][col]
                        stateCopy[row][col]=""
                        if('N' in color):
                            score = self.minimax(stateCopy,depth-1,not playerMove,"Blanco")
                        else:
                            score = self.minimax(stateCopy,depth-1,not playerMove,"Negro")
                        score[0], score[1] = (row,col),(x,y)      

                        if not playerMove:
                            if score[2] > best[2]:
                                best = score  # max value
                        else:
                            if score[2] < best[2]:
                                best = score  # min value
        return best	

  
    def play(self,board,color):
        state=copyBoard(board)
        move=self.minimax(state,4,False,color)
        return move

    def getStateValue(self,state,myCol):
        if myCol=='N':
            myCol='N'
            enemyCol='B'
        else:
            myCol='B'
            enemyCol='N'       
        res=0
        res+=self.getStateValueAux(state,myCol)
        res-=(self.getStateValueAux(state,enemyCol))*(6/8)          
        return res
    
    def getStateValueAux(self,state,myCol):    
        res=0
        isMyKing =False
        for row in state:
            for col in row:
                if(myCol in col):
                    res+=getPieceValue(col)     
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
        return 1000
    else:
        return 0
