import pygame

whitePieces = ["BP","BR","BD","BA","BC","BT"]
blackPieces = ["NP","NR","ND","NA","NC","NT"]

class Rules:
    def IsCheckmate(self,board,color):
            #returns true if 'color' player is in checkmate
            #Call GetListOfValidMoves for each piece of current player
            #If there aren't any valid moves for any pieces, then return true

            if color == "Negro":
                    myColor = 'N'
                    enemyColor = 'B'
            else:
                    myColor = 'B'
                    enemyColor = 'N'

            myColorValidMoves = [];
            for row in range(8):
                    for col in range(8):
                            piece = board[row][col]
                            if myColor in piece:
                                    myColorValidMoves.extend(self.GetListOfValidMoves(board,color,(row,col)))

            if len(myColorValidMoves) == 0:
                    return True
            else:
                    return False

    def GetListOfValidMoves(self,board,color,fromTuple):
            legalDestinationSpaces = []
            if('T' in board[fromTuple[0]][fromTuple[1]]):
                for row in range(8):
                        d =(row,fromTuple[1]) 
                        if self.IsLegalMove(board[fromTuple[0]][fromTuple[1]],board,fromTuple,d):
                                if not self.DoesMovePutPlayerInCheck(board,color,fromTuple,d):
                                        legalDestinationSpaces.append(d)
                for col in range(8):
                        d =(fromTuple[0],col) 
                        if self.IsLegalMove(board[fromTuple[0]][fromTuple[1]],board,fromTuple,d):
                                if not self.DoesMovePutPlayerInCheck(board,color,fromTuple,d):
                                        legalDestinationSpaces.append(d)
            else:
                for row in range(8):
                        for col in range(8):
                                d = (row,col)
                                if self.IsLegalMove(board[fromTuple[0]][fromTuple[1]],board,fromTuple,d):
                                        if not self.DoesMovePutPlayerInCheck(board,color,fromTuple,d):
                                                legalDestinationSpaces.append(d)
            return legalDestinationSpaces
	    
    def IsLegalMove(self,sprite,board,fromTuple,toTuple):
        fromSquare_r = fromTuple[0]
        fromSquare_c = fromTuple[1]
        toSquare_r = toTuple[0]
        toSquare_c = toTuple[1]
        fromPiece = board[fromSquare_r][fromSquare_c]
        toPiece = board[toSquare_r][toSquare_c]
        if fromTuple == toTuple:
            return False
        if sprite == "NP":
            if toSquare_r == fromSquare_r+1 and toSquare_c == fromSquare_c and toPiece == "":
                return True
            if fromSquare_r == 1 and toSquare_r == fromSquare_r+2 and toSquare_c == fromSquare_c and toPiece == "":
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True
            if toSquare_r == fromSquare_r+1 and (toSquare_c == fromSquare_c+1 or toSquare_c == fromSquare_c-1) and (toPiece in whitePieces):
                return True
             
        elif (sprite == "BP"):
            if toSquare_r == fromSquare_r-1 and toSquare_c == fromSquare_c and toPiece == "":
                return True
            if fromSquare_r == 6 and toSquare_r == fromSquare_r-2 and toSquare_c == fromSquare_c and toPiece == "":
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True
            if toSquare_r == fromSquare_r-1 and (toSquare_c == fromSquare_c+1 or toSquare_c == fromSquare_c-1) and (toPiece in blackPieces):
                return True
            
        elif (sprite == "BT"):
            if (toSquare_r == fromSquare_r or toSquare_c == fromSquare_c) and (toPiece == "" or (toPiece in blackPieces)):
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True
        elif (sprite == "NT"):
            if (toSquare_r == fromSquare_r or toSquare_c == fromSquare_c) and (toPiece == "" or (toPiece in whitePieces)):
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True;
                
        elif "BC" in fromPiece:
            col_diff = toSquare_c - fromSquare_c
            row_diff = toSquare_r - fromSquare_r
            if toPiece == "" or toPiece in blackPieces:
                if col_diff == 1 and row_diff == -2:
                    return True
                if col_diff == 2 and row_diff == -1:
                    return True
                if col_diff == 2 and row_diff == 1:
                    return True
                if col_diff == 1 and row_diff == 2:
                    return True
                if col_diff == -1 and row_diff == 2:
                    return True
                if col_diff == -2 and row_diff == 1:
                    return True
                if col_diff == -2 and row_diff == -1:
                    return True
                if col_diff == -1 and row_diff == -2:
                    return True
        elif "NC" in fromPiece:
            col_diff = toSquare_c - fromSquare_c
            row_diff = toSquare_r - fromSquare_r
            if toPiece == "" or toPiece in whitePieces:
                if col_diff == 1 and row_diff == -2:
                    return True
                if col_diff == 2 and row_diff == -1:
                    return True
                if col_diff == 2 and row_diff == 1:
                    return True
                if col_diff == 1 and row_diff == 2:
                    return True
                if col_diff == -1 and row_diff == 2:
                    return True
                if col_diff == -2 and row_diff == 1:
                    return True
                if col_diff == -2 and row_diff == -1:
                    return True
                if col_diff == -1 and row_diff == -2:
                    return True

        elif "BA" in fromPiece:
            if ( abs(toSquare_r - fromSquare_r) == abs(toSquare_c - fromSquare_c) ) and (toPiece == "" or ( toPiece in blackPieces)):
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True
        elif "NA" in fromPiece:
            if ( abs(toSquare_r - fromSquare_r) == abs(toSquare_c - fromSquare_c) ) and (toPiece == "" or ( toPiece in whitePieces)):
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True
                
        elif "BD" in fromPiece:
            if (toSquare_r == fromSquare_r or toSquare_c == fromSquare_c) and (toPiece == "" or (toPiece in blackPieces)):
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True
            if ( abs(toSquare_r - fromSquare_r) == abs(toSquare_c - fromSquare_c) ) and (toPiece == "" or ( toPiece in blackPieces)):
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True
        elif "ND" in fromPiece:
            if (toSquare_r == fromSquare_r or toSquare_c == fromSquare_c) and (toPiece == "" or (toPiece in whitePieces)):
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True
            if ( abs(toSquare_r - fromSquare_r) == abs(toSquare_c - fromSquare_c) ) and (toPiece == "" or ( toPiece in whitePieces)):
                if self.IsClearPath(board,fromTuple,toTuple):
                    return True

        elif "BR" in fromPiece:
            col_diff = toSquare_c - fromSquare_c
            row_diff = toSquare_r - fromSquare_r
            if toPiece == "" or ( toPiece in blackPieces):
                if abs(col_diff) == 1 and abs(row_diff) == 0:
                    return True
                if abs(col_diff) == 0 and abs(row_diff) == 1:
                    return True
                if abs(col_diff) == 1 and abs(row_diff) == 1:
                    return True            
        elif "NR" in fromPiece:
            col_diff = toSquare_c - fromSquare_c
            row_diff = toSquare_r - fromSquare_r
            if toPiece == "" or ( toPiece in whitePieces):
                if abs(col_diff) == 1 and abs(row_diff) == 0:
                    return True
                if abs(col_diff) == 0 and abs(row_diff) == 1:
                    return True
                if abs(col_diff) == 1 and abs(row_diff) == 1:
                    return True
        else:
            return False

    def IsClearPath(self,board,fromTuple,toTuple):
        #Return true if there is nothing in a straight line between fromTuple and toTuple, non-inclusive
        #Direction could be +/- vertical, +/- horizontal, +/- diagonal
        fromSquare_r = fromTuple[0]
        fromSquare_c = fromTuple[1]
        toSquare_r = toTuple[0]
        toSquare_c = toTuple[1]
        fromPiece = board[fromSquare_r][fromSquare_c]

        if abs(fromSquare_r - toSquare_r) <= 1 and abs(fromSquare_c - toSquare_c) <= 1:
            #The base case: just one square apart
            return True
        else:
            if toSquare_r > fromSquare_r and toSquare_c == fromSquare_c:
                #vertical +
                newTuple = (fromSquare_r+1,fromSquare_c)
            elif toSquare_r < fromSquare_r and toSquare_c == fromSquare_c:
                #vertical -
                newTuple = (fromSquare_r-1,fromSquare_c)
            elif toSquare_r == fromSquare_r and toSquare_c > fromSquare_c:
                #horizontal +
                newTuple = (fromSquare_r,fromSquare_c+1)
            elif toSquare_r == fromSquare_r and toSquare_c < fromSquare_c:
                #horizontal -
                newTuple = (fromSquare_r,fromSquare_c-1)
            elif toSquare_r > fromSquare_r and toSquare_c > fromSquare_c:
                #diagonal "SE"
                newTuple = (fromSquare_r+1,fromSquare_c+1)
            elif toSquare_r > fromSquare_r and toSquare_c < fromSquare_c:
                #diagonal "SW"
                newTuple = (fromSquare_r+1,fromSquare_c-1)
            elif toSquare_r < fromSquare_r and toSquare_c > fromSquare_c:
               #diagonal "NE"
                newTuple = (fromSquare_r-1,fromSquare_c+1)
            elif toSquare_r < fromSquare_r and toSquare_c < fromSquare_c:
                #diagonal "NW"
                newTuple = (fromSquare_r-1,fromSquare_c-1)

        if board[newTuple[0]][newTuple[1]] != "":
            return False
        else:
            return self.IsClearPath(board,newTuple,toTuple)
        
    def DoesMovePutPlayerInCheck(self,board,color,fromTuple,toTuple):
            #makes a hypothetical move; returns True if it puts current player into check
            fromSquare_r = fromTuple[0]
            fromSquare_c = fromTuple[1]
            toSquare_r = toTuple[0]
            toSquare_c = toTuple[1]
            fromPiece = board[fromSquare_r][fromSquare_c]
            toPiece = board[toSquare_r][toSquare_c]

            #make the move, then test if 'color' is in check
            board[toSquare_r][toSquare_c] = fromPiece
            board[fromSquare_r][fromSquare_c] = ""

            retval = self.IsInCheck(board,color)

            #undo temporary move
            board[toSquare_r][toSquare_c] = toPiece
            board[fromSquare_r][fromSquare_c] = fromPiece

            return retval

    def IsInCheck(self,board,color):
            #check if 'color' is in check
            #scan through squares for all enemy pieces; if there IsLegalMove to color's king, then return True.
            if color == "Negro":
                    myColor = 'N'
                    enemyColor = 'B'
                    enemyColorFull = "Negro"
            else:
                    myColor = 'B'
                    enemyColor = 'N'
                    enemyColorFull = "Blanco"

            kingTuple = (0,0)
            #First, get current player's king location
            #if(var):
             #   print("myColor",myColor)
            for row in range(8):
                    for col in range(8):
                            piece = board[row][col]
                            if 'R' in piece and myColor in piece:
                                    kingTuple = (row,col)
            #Check if any of enemy player's pieces has a legal move to current player's king
            for row in range(8):
                    for col in range(8):
                            piece = board[row][col]
                            if enemyColor in piece:
                                    if self.IsLegalMove(piece,board,(row,col),kingTuple):
                                            return True
            return False
        
def printM(matrix):
    for i in matrix:
        for j in i:
            if j=="":
                print("__", end=" ")
            else:
                print(j,end=" ")
        print()
        
