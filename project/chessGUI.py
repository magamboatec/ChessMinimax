import pygame
from Rules import Rules

pygame.init()

blackColor = (0,0,0)
gameDisplay = pygame.display.set_mode((1000,500),0,32)
pygame.display.set_caption("Chess solver")
gameDisplay.fill((0,0,0))
clock = pygame.time.Clock()

whitePlayer = True

negReyImg = pygame.transform.scale(pygame.image.load("images//NR.png"),(50,50))
blaReyImg = pygame.transform.scale(pygame.image.load("images//BR.png"),(50,50))
negTorImg = pygame.transform.scale(pygame.image.load("images//NT.png"),(50,50))
blaTorImg = pygame.transform.scale(pygame.image.load("images//BT.png"),(50,50))
negCabImg = pygame.transform.scale(pygame.image.load("images//NC.png"),(50,50))
blaCabImg = pygame.transform.scale(pygame.image.load("images//BC.png"),(50,50))
negAlfImg = pygame.transform.scale(pygame.image.load("images//NA.png"),(50,50))
blaAlfImg = pygame.transform.scale(pygame.image.load("images//BA.png"),(50,50))
negDamImg = pygame.transform.scale(pygame.image.load("images//ND.png"),(50,50))
blaDamImg = pygame.transform.scale(pygame.image.load("images//BD.png"),(50,50))
negPeoImg = pygame.transform.scale(pygame.image.load("images//NP.png"),(50,50))
blaPeoImg = pygame.transform.scale(pygame.image.load("images//BP.png"),(50,50))
brownSquare = pygame.image.load("images//brown_square.png")
whiteSquare = pygame.image.load("images//white_square.png")
cyanSquare = pygame.image.load("images//cyan_square.png")

blackPieces = [negReyImg,negTorImg,negCabImg,negAlfImg,negDamImg,negPeoImg]
whitePieces = [blaReyImg,blaTorImg,blaCabImg,blaAlfImg,blaDamImg,blaPeoImg]

gameMatrix =  [[(50,50),(100,50),(150,50),(200,50),(250,50),(300,50),(350,50),(400,50)],
              [(50,100),(100,100),(150,100),(200,100),(250,100),(300,100),(350,100),(400,100)],
              [(50,150),(100,150),(150,150),(200,150),(250,150),(300,150),(350,150),(400,150)],
              [(50,200),(100,200),(150,200),(200,200),(250,200),(300,200),(350,200),(400,200)],
              [(50,250),(100,250),(150,250),(200,250),(250,250),(300,250),(350,250),(400,250)],
              [(50,300),(100,300),(150,300),(200,300),(250,300),(300,300),(350,300),(400,300)],
              [(50,350),(100,350),(150,350),(200,350),(250,350),(300,350),(350,350),(400,350)],
              [(50,400),(100,400),(150,400),(200,400),(250,400),(300,400),(350,400),(400,400)]]

spritesMatrix = [["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""]]

piecesMatrix = [["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""]]

spritesMatrix[0][4] = blaReyImg
spritesMatrix[6][2] = negReyImg
spritesMatrix[2][4] = blaPeoImg
spritesMatrix[0][0] = blaTorImg
spritesMatrix[3][5] = negDamImg
spritesMatrix[6][6] = negPeoImg

piecesMatrix[0][4] = "br"
piecesMatrix[6][2] = "nr"
piecesMatrix[2][4] = "bp"
piecesMatrix[3][5] = "nd"
piecesMatrix[6][6] = "np"

#Imprime el tablero de juego
def printMatrix():
    control = True
    for i in gameMatrix:
        for j in i:
            if control:
                gameDisplay.blit(brownSquare,j)
            else:
                gameDisplay.blit(whiteSquare,j)
            control= not(control)    
        control= not(control)
#coloca las piesas
def fill(matrix):
    for fil in range(8):
        for col in range(8):
            if spritesMatrix[fil][col]!="":
                gameDisplay.blit(matrix[fil][col],gameMatrix[fil][col])
                
#dado cordenadas x y se retorna la posicion
#de la piesa en la matriz
def buscarIndice(xIn,yIn):
    for fil in range(8):
        for col in range(8):
            if(gameMatrix[fil][col]==(xIn,yIn)):
                return (fil,col)
    return (-1,-1)

#redondea al multiplo de 50 inferior
def roundBy50(x):
    return int(x) - int(x) % 50

def moveAnimation(sprite,x,y,xMeta,yMeta,tempMatrix):
    count = 0
    
    fill(tempMatrix)
#    print("iniX: ",x," iniY: ",y)
#    print("meta:(",xMeta,yMeta,")")
    while x!=xMeta or y!=yMeta:
        if x<xMeta:
            x+=10
        elif x>xMeta:
            x-=10
            
        if y<yMeta:
            y+=10
        elif y>yMeta:
            y-=10
        printMatrix()
        fill(tempMatrix)
        gameDisplay.blit(sprite,(x,y))
        pygame.display.update()
        clock.tick(30)
        count+=1
        if count>100:
            break
        
def printM(matrix):
    for i in matrix:
        for j in i:
            if j=="":
                print("0", end=" ")
            else:
                print("1",end=" ")
        print()


def spriteName(sprite):
    if sprite==negReyImg or sprite==blaReyImg:
        return "R"
    elif sprite==negTorImg or sprite==blaTorImg:
        return "T"
    elif sprite==negCabImg or sprite==blaCabImg:
        return "C"
    elif sprite==negAlfImg or sprite==blaAlfImg:
        return "A"
    elif sprite==negDamImg or sprite==blaDamImg:
        return "D"
    elif sprite==negPeoImg or sprite==blaPeoImg:
        return "P"
    else:
        return ""
"""
ciclo de ejecucion
"""
def execute():
    global spritesMatrix,piecesMatrix,whitePlayer
    catched= False #permite saber si ya ha elegido una pieza
    sprite=""
    piece =""
    done = False
    iniX =0
    iniY =0
    iniPosI=0
    iniPosJ=0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            coorX=roundBy50(pygame.mouse.get_pos()[0])
            coorY=roundBy50(pygame.mouse.get_pos()[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(event.button == 3):
                    catched= False
                loc=buscarIndice(coorX,coorY)    
                if(loc!=(-1,-1)):
                    if(not catched):
                        iniPosI=loc[0]
                        iniPosJ=loc[1]
                        iniX = coorX
                        iniY = coorY
                        sprite= spritesMatrix[loc[0]][loc[1]]
                        piece = piecesMatrix[loc[0]][loc[1]]
                        if(sprite!=""):
                            if(whitePlayer):
                                if(sprite in whitePieces):
                                    catched=True
                            else:
                                if(sprite in blackPieces):
                                    catched=True                                
                    else:
                        
                        if(Rules.IsLegalMove(piece,piecesMatrix,(iniPosI,iniPosJ),(loc[0],loc[1]))):
                           print("sii")
                        spritesMatrix[iniPosI][iniPosJ]=""
                        moveAnimation(sprite,iniX,iniY,coorX,coorY,spritesMatrix)
                        spritesMatrix[loc[0]][loc[1]]=sprite
                        piecesMatrix[loc[0]][loc[1]]=piece
                        iniX = 0
                        iniY = 0
                        iniPosI=0
                        iniPosJ=0
                        catched=False
                        whitePlayer=not whitePlayer
                    
        printMatrix()
        if(catched):
            gameDisplay.blit(cyanSquare,(iniX,iniY));
            
        fill(spritesMatrix)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()    
    
execute()
