from Rules import Rules
import random
from math import inf
import time
import random

class AI:
    def __init__(self):
        self.rules = Rules()
        self.alpha = [(),(),-inf]
        self.beta = [(),(),inf]
        self.missedPieces =[]
        self.color=""
           
    def negaMin(self,state,depth,color,alpha,beta):
        if 'N' in color:
            enemyColor="Blanco"
        else:
            enemyColor="Negro"        
        if(depth==0):
            return [(),(),self.getStateValue(state,enemyColor)]
        best=[(),(),inf-1]
        for row in range(8):
            for col in range(8):
                if color[0] in state[row][col]:
                    moves = self.rules.GetListOfValidMoves(state,color,(row,col))
                    for move in moves:
                        x, y = move[0], move[1]
                        score=[(),(),0]
                        newState=self.doMove(state,(row,col),(x,y))
                        score[2] = -self.negaMin(newState,depth-1,enemyColor,[(),(),-beta[2]],[(),(),-alpha[2]])[2]       
                        score[0], score[1] = (row,col),(x,y)
                        if(score[2]<best[2]):
                            best=score
                        if(best[2]<alpha[2]):
                            alpha=best
                        if(best[2]<=beta[2]):
                            break                                
                            
        return best

    def play(self,board,color):
        self.color = color
        state=copyBoard(board)
        start_time = time.time()
        depth=4
        while depth>0:
            move = self.negaMin(state,depth,color,[(),(),inf],[(),(),-inf])
            if move[0]!=() and move[2]!=+inf:
                break
            depth-=1
        #print("--- %s seconds ---" % (time.time() - start_time))
        return move
    

    def getStateValue(self,state,myColFull):
            
        if 'N' in myColFull:
            enemyCol = 'B'
            myCol = 'N'
        else:
            enemyCol = 'N'
            myCol = 'B'      
        bishopCount = 0 
        res=0
        for row in range(8):
            for col in range(8):
                piece=state[row][col]
                if(myCol in piece):
                    res+=self.getPieceValue(piece,row,col,state)
                    if('A' in piece):
                        bishopCount+=1
                elif(enemyCol in piece):
                    res-=self.getPieceValue(piece,row,col,state)*0.5
        if(bishopCount==2):
            res+=25
        return res
    
    
    def doMove(self,board,posIni,posFin):
        tempBoard = copyBoard(board)
        piece = tempBoard[posIni[0]][posIni[1]]
        if('P'in piece):
            if('N' in piece):
                if(posFin[0]==7):
                    piece="ND"
            else:   
                if(posFin[0]==0):
                    piece="BD"
        tempBoard[posIni[0]][posIni[1]] = ""
        tempBoard[posFin[0]][posFin[1]] = piece
        return tempBoard



    def getPieceValue(self,piece,row,col,state):
        if('N' in piece):
            myColor = 'N'
        else:
            myColor = 'B'
            
        if ('P' in piece):
            res = 100
            if('N'==myColor):
                res+=row
                if(row==7):
                    return 900
                if(self.rules.IsClearPath(state,(row,col),(7,col))):
                    res+=20
                if(col!=0):
                    if ('N' in state[row+1][col-1]):
                        res+=10
                if(col!=7):
                    if('N' in state[row+1][col+1]):
                        res+=10                                                        
            else:
                res+=(7-row)
                if(row==0):
                    return 900                
                if(self.rules.IsClearPath(state,(row,col),(0,col))):
                    res+=20
                if(col!=0):
                    if ('B' in state[row-1][col-1]):
                        res+=10
                if(col!=7):
                    if('B' in state[row-1][col+1]):
                        res+=10                        
            if(isCenter(row,col)):
                res+=40
            return res
        elif('R' in piece):
            res=0
            if(col!=0):
                if(myColor in state[row][col-1]):
                    res+=10
                elif('' in state[row][col-1]):
                    res+=5                    
                if(row!=0):
                    if(myColor in state[row-1][col-1]):
                        res+=10
                    elif('' in state[row-1][col-1]):
                        res+=5
                if(row!=7):
                    if(myColor in state[row+1][col-1]):
                        res+=10
                    elif('' in state[row+1][col-1]):
                        res+=5                        
            if(col!=7):
                if(myColor in state[row][col+1]):
                    res+=10
                elif('' in state[row][col+1]):
                    res+=5
                if(row!=0):
                    if(myColor in state[row-1][col+1]):
                        res+=10
                    elif('' in state[row-1][col+1]):
                        res+=5                        
                if(row!=7):
                    if(myColor in state[row+1][col+1]):
                        res+=10
                    elif('' in state[row+1][col+1]):
                        res+=5                        
            if(row!=7):
                if(myColor in state[row+1][col]):
                    res+=10
                elif('' in state[row+1][col]):
                    res+=5
            if(row!=0):
                if(myColor in state[row-1][col]):
                    res+=10
                elif('' in state[row-1][col]):
                    res+=5
            if(row==0 and col==4 and myColor=='N'):
                res+=15
            if(row==7 and col==4 and myColor=='B'):
                res+=15                                
            return res
        
        elif('C' in piece) :
            res = 300
            if(isCenter(row,col)):
                res+=20
            if(col!=7 and col!=6):
                if(row!=0):
                    if(myColor in state[row-1][col+2]):
                        res+=10
                    elif('' in state[row-1][col+2]):
                        res+=5
                if(row!=7):
                    if(myColor in state[row+1][col+2]):
                        res+=10
                    elif('' in state[row+1][col+2]):
                        res+=5
            if(col!=0 and col!=1):
                if(row!=0):
                    if(myColor in state[row-1][col-2]):
                        res+=10
                    elif('' in state[row-1][col-2]):
                        res+=5                        
                if(row!=7):
                    if(myColor in state[row+1][col-2]):
                        res+=10
                    elif('' in state[row+1][col-2]):
                        res+=5
            if(row!=0 and row!=1):
                if(col!=0):
                    if(myColor in state[row-2][col-1]):
                        res+=10
                    elif('' in state[row-2][col-1]):
                        res+=5                        
                if(col!=7):
                    if(myColor in state[row-2][col+1]):
                        res+=10
                    elif('' in state[row-2][col+1]):
                        res+=5                        
            if(row!=7 and row!=6):
                if(col!=0):
                    if(myColor in state[row+2][col-1]):
                        res+=10
                    elif('' in state[row+2][col-1]):
                        res+=5                        
                if(col!=7):
                    if(myColor in state[row+2][col+1]):
                        res+=10
                    elif('' in state[row+2][col+1]):
                        res+=5
            return res
        elif('A' in piece):
            res = 310
            if(isCenter(row,col)):
                res+=20
            if('N'==myColor):
                if(row==0):
                    res-=15
            else:
                if(row==7):
                    res-=15
            return res
        elif('T' in piece):
            res = 500
            if('N'==myColor):
                if(row==6):
                    res+=20
            else:
                if(row==1):
                    res+=20            
            return res
        elif ('D' in piece):
            res =  900
            if(isCenter(row,col)):
                res+=30            
            return res
        else:
            return 0
def isCenter(row,col):
    if (row==3 and (col==3 or col==4)):
        return True
    elif (row==4 and (col==3 or col==4)):
        return True
    else:
        return False
    
def getMaxState(states):
    best = states[0]
    for i in states:
        if(i[2]>best[2]):
            best=i
    return best        

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
        

