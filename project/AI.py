from Rules import Rules
import random
from math import inf
import time

class AI:
    def __init__(self):
        self.rules = Rules()
        self.alpha = [(),(),-inf]
        self.beta = [(),(),inf]
        self.missedPieces =[]

    def minimax2(self,state,depth,playerMove,color):
        if not playerMove:
            best = [(), (), -inf]
        else:
            best = [(), (), +inf]

        if depth == 0:
            if 'N' in color:
                color = "Blanco"
            else:
                color = "Negro"
            value = self.getStateValue(state,color)
            return [(), (), value]

        for row in range(8):
            for col in range(8):
                if color[0] in state[row][col]:
                    for move in self.rules.GetListOfValidMoves(state,color,(row,col)):
                        stateCopy=copyBoard(state)
                        x, y = move[0], move[1]
                        stateCopy[x][y] = state[row][col]
                        stateCopy[row][col]=""
                        if('N' in color):
                            score = self.minimax2(stateCopy,depth-1,not playerMove,"Blanco")
                        else:
                            score = self.minimax2(stateCopy,depth-1,not playerMove,"Negro")   
                        score[0], score[1] = (row,col),(x,y)      
                        if not playerMove:
                            if score[2] > best[2]:
                                best = score  # max value
                            if best[2] > self.alpha[2]:
                                self.alpha = best
                        else:
                            self.alpha = [(),(),-inf]
                            if score[2] < best[2]:
                                best = score  # min value
                            if best[2] < self.beta[2]:
                                self.beta = best
                        if self.beta[2]-self.alpha[2]<=0:
                            return best
        if not playerMove:
            self.alpha = [(),(),-inf]
        else:
            self.beta = [(),(),inf]
        return best
                        
    def minimax(self,state,depth,playerMove,color):
        if not playerMove:
            best = [(), (), -inf]
        else:
            best = [(), (), +inf]

        if depth == 0:
            if 'N' in color:
                color = "Blanco"
            else:
                color = "Negro"
            value = self.getStateValue(state,color)
            return [(), (), value]
        
        for row in range(8):
            for col in range(8):
                if color[0] in state[row][col]:
                    for move in self.rules.GetListOfValidMoves(state,color,(row,col)):
                        stateCopy=copyBoard(state)
                        x, y = move[0], move[1]
                        stateCopy[x][y] = state[row][col]
                        stateCopy[row][col]=""
                        if('N' in color):
                            score = self.minimax(stateCopy,depth-1,not playerMove,"Blanco")
                        else:
                            score = self.minimax(stateCopy,depth-1,not playerMove,"Negro")   
                        score[0], score[1] = (row,col),(x,y)      
                        if not playerMove:
                            if score[2] >= best[2]:
                                best = score  # max value
                            if best[2] >= self.alpha[2]:
                                self.alpha = best
                        else:
                            if score[2] <= best[2]:
                                best = score  # min value
                            if best[2] <= self.beta[2]:
                                self.beta = best
                        if self.beta[2]<=self.alpha[2]:
                            return best

        if not playerMove:
            self.alpha = [(),(),-inf]
        else:
            self.beta = [(),(),inf]
        return best         
    def play(self,board,color):
        state=copyBoard(board)
        start_time = time.time()
        move=self.minimax2(state,3,False,color)
        print("--- %s seconds ---" % (time.time() - start_time))
        self.alpha = [(),(),-inf]
        self.beta = [(),(),inf]
        return move

    def getStateValue(self,state,myColFull):
        if myColFull=="Negro":
            enemyColFull="Blanco"
        else:
            enemyColFull="Negro"       
        res=0
        res+=self.getStateValueAux(state,myColFull,enemyColFull)        
        res-=(self.getStateValueAux(state,enemyColFull,myColFull))*(1/2)
        return res
    
    def getStateValueAux(self,state,myCol,enemyCol):
        res=0
        for row in range(8):
            for col in range(8):
                if(myCol[0] in state[row][col]):
                    res+=self.getPieceValue(state[row][col],row)
        return res
    
    def getMove(self,board,posIni,posFin):
        tempBoard = copyBoard(board)
        piece = tempBoard[posIni[0]][posIni[1]] 
        tempBoard[posIni[0]][posIni[1]] = ""
        tempBoard[posFin[0]][posFin[1]] = piece
        return tempBoard


    def getMaxMissedPiece(self):
        values = []
        for i in range(len(self.missedPieces)):
            values.append(self.getPieceValue(self.missedPieces[i],0))

        maxInd=values.index(max(values))
        
        return self.missedPieces[maxInd]

    def getPieceValue(self,piece,row):
        if ('P' in piece):
            if len(self.missedPieces)>0:
                if('N' in piece):
                    return (row)*0.02
                else:
                    return (8-row)*0.02
            else:
                return 1
        elif('A' in piece) or ('C' in piece) :
            return 3
        elif('T' in piece):
            return 5
        elif ('D' in piece):
            return 9
        else:
            return 0

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
        

