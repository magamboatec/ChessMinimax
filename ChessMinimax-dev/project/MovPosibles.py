from Rules import Rules

class MovPosibles:
    def movimientosposibles(self,piece,piecesMatrix,Pos):
        movimientos = []
        rules = Rules()
        for i in range(8):
            for j in range(8):
                if(rules.IsLegalMove(piece,piecesMatrix,(Pos[0],Pos[1]),(i,j))==True):
                    movimientos.append((i,j))
                j = j + 1
            i = i + 1
        return movimientos
