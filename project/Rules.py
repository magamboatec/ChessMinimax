import pygame


class Rules:

    def IsLegalMove(sprite,board,fromTuple,toTuple):
        fromSquare_r = fromTuple[0]
        fromSquare_c = fromTuple[1]
        toSquare_r = toTuple[0]
        toSquare_c = toTuple[1]
        fromPiece = board[fromSquare_r][fromSquare_c]
        toPiece = board[toSquare_r][toSquare_c]

        if fromTuple == toTuple:
            return False
        if sprite == "P":
            print("NegPeo")
            if toSquare_r == fromSquare_r+1 and toSquare_c == fromSquare_c and toPiece == "":
                #moving forward one space
                return True
            if fromSquare_r == 1 and toSquare_r == fromSquare_r+2 and toSquare_c == fromSquare_c and toPiece == "":
                    #black pawn on starting row can move forward 2 spaces if there is no one directly ahead
                   # if self.IsClearPath(board,fromTuple,toTuple):
                return True
            #if toSquare_r == fromSquare_r+1 and (toSquare_c == fromSquare_c+1 or toSquare_c == fromSquare_c-1) and enemyColor in toPiece:
                #attacking
             #   return True
             
        elif (sprite == "P"):
            print("BlaPeo")
            if toSquare_r == fromSquare_r-1 and toSquare_c == fromSquare_c and toPiece == "":
                #moving forward one space
                return True
            if fromSquare_r == 6 and toSquare_r == fromSquare_r-2 and toSquare_c == fromSquare_c and toPiece == "":
                #black pawn on starting row can move forward 2 spaces if there is no one directly ahead
                   # if self.IsClearPath(board,fromTuple,toTuple):
                return True
            #if toSquare_r == fromSquare_r-1 and (toSquare_c == fromSquare_c+1 or toSquare_c == fromSquare_c-1) and enemyColor in toPiece:
                    #attacking
             #       return True

        return False #if none of the other "True"s are hit above
