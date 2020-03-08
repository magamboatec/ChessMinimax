import pygame
from Rules import Rules
from ScrollingTextBox import ScrollingTextBox

pygame.init()
pygame.mixer.init()
music=pygame.mixer.music.load("file.mp3")
catchSound=pygame.mixer.Sound("catch.wav")
pygame.mixer.music.set_volume(0.05)
catchSound.set_volume(0.2)
pygame.mixer.music.play(-1)

blackColor = (0,0,0)
gameDisplay = pygame.display.set_mode((1200,760),0,32)
pygame.display.set_caption("Chess solver")
gameDisplay.fill((0,0,0))
clock = pygame.time.Clock()
rules = Rules()

whitePlayer = True

negReyImg = pygame.transform.scale(pygame.image.load("images//NR.png"),(75,75))
blaReyImg = pygame.transform.scale(pygame.image.load("images//BR.png"),(75,75))
negTorImg = pygame.transform.scale(pygame.image.load("images//NT.png"),(75,75))
blaTorImg = pygame.transform.scale(pygame.image.load("images//BT.png"),(75,75))
negCabImg = pygame.transform.scale(pygame.image.load("images//NC.png"),(75,75))
blaCabImg = pygame.transform.scale(pygame.image.load("images//BC.png"),(75,75))
negAlfImg = pygame.transform.scale(pygame.image.load("images//NA.png"),(75,75))
blaAlfImg = pygame.transform.scale(pygame.image.load("images//BA.png"),(75,75))
negDamImg = pygame.transform.scale(pygame.image.load("images//ND.png"),(75,75))
blaDamImg = pygame.transform.scale(pygame.image.load("images//BD.png"),(75,75))
negPeoImg = pygame.transform.scale(pygame.image.load("images//NP.png"),(60,60))
blaPeoImg = pygame.transform.scale(pygame.image.load("images//BP.png"),(60,60))
brownSquare = pygame.transform.scale(pygame.image.load("images//brown_square.jpg"),(75,75))
whiteSquare = pygame.transform.scale(pygame.image.load("images//white_square.jpg"),(75,75))
cyanSquare = pygame.transform.scale(pygame.image.load("images//blue_square.jpg"),(75,75))
bordeImg = pygame.transform.scale(pygame.image.load("images//borde.png"),(690,690))
fondoImg = pygame.image.load("images//fondo.jpg")

blackPieces = [negReyImg,negTorImg,negCabImg,negAlfImg,negDamImg,negPeoImg]
whitePieces = [blaReyImg,blaTorImg,blaCabImg,blaAlfImg,blaDamImg,blaPeoImg]

gameMatrix =  [[(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(600,75)],
              [(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(600,150)],
              [(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(600,225)],
              [(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(600,300)],
              [(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(600,375)],
              [(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(600,450)],
              [(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525),(600,525)],
              [(75,600),(150,600),(225,600),(300,600),(375,600),(450,600),(525,600),(600,600)]]

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
spritesMatrix[1][4] = blaAlfImg
spritesMatrix[6][2] = negReyImg
spritesMatrix[2][4] = blaPeoImg
spritesMatrix[0][0] = blaTorImg
spritesMatrix[3][5] = negDamImg
spritesMatrix[6][6] = negPeoImg
spritesMatrix[1][1] = negCabImg

piecesMatrix[0][4] = "BR"
piecesMatrix[1][4] = "BA"
piecesMatrix[6][2] = "NR"
piecesMatrix[2][4] = "BP"
piecesMatrix[3][5] = "ND"
piecesMatrix[6][6] = "NP"
piecesMatrix[0][0] = "BT"
piecesMatrix[1][1] = "NC"

gameDisplay.blit(fondoImg,(0,0))
gameDisplay.blit(bordeImg,(30,30))

movesCount=1


def printMessage(message):
    #prints a string to the area to the right of the board
    textBox.Add(message)
    textBox.Draw()
    
textBox = ScrollingTextBox(gameDisplay,850,1100,30,750)

def converIndCol(num):
    if num==0:
        return 'a'
    if num==1:
        return 'b'
    if num==2:
        return 'c'
    if num==3:
        return 'd'
    if num==4:
        return 'e'
    if num==5:
        return 'f'
    if num==6:
        return 'g'
    if num==7:
        return 'h'

def converIndFil(num):
    if num==0:
        return '8'
    if num==1:
        return '7'
    if num==2:
        return '6'
    if num==3:
        return '5'
    if num==4:
        return '4'
    if num==5:
        return '3'
    if num==6:
        return '2'
    if num==7:
        return '1'
    
        
def drawMarkets():
    white = (255, 255, 255)
    markersA = ["a","b","c","d","e","f","g","h"]
    markersB = ["8","7","6","5","4","3","2","1"]
    x=39
    y=40
    font = pygame.font.Font('freesansbold.ttf', 30)
    for i in markersA:
        x+=75
        text = font.render(i, True, white)
        textRect = text.get_rect()
        #textRect.center = (x,60)
        #gameDisplay.blit(text, textRect)
        textRect.center = (x,737)
        gameDisplay.blit(text, textRect)
    for i in markersB:
        y+=75
        text = font.render(i, True, white)
        textRect = text.get_rect()
        #textRect.center = (x,60)
        #gameDisplay.blit(text, textRect)
        textRect.center = (20,y)
        gameDisplay.blit(text, textRect)        
    
drawMarkets()
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
                if(spritesMatrix[fil][col]==negPeoImg or spritesMatrix[fil][col]==blaPeoImg):
                    gameDisplay.blit(matrix[fil][col],(gameMatrix[fil][col][0]+10,gameMatrix[fil][col][1]+15))
                else:    
                    gameDisplay.blit(matrix[fil][col],gameMatrix[fil][col])
      
#dado cordenadas x y se retorna la posicion
#de la piesa en la matriz
def buscarIndice(xIn,yIn):
    for fil in range(8):
        for col in range(8):
            if(gameMatrix[fil][col]==(xIn,yIn)):
                return (fil,col)
    return (-1,-1)

#redondea al multiplo de 75 inferior
def roundBy75(x):
    return int(x) - int(x) % 75

def moveAnimation(sprite,x,y,xMeta,yMeta,tempMatrix):
    count = 0
    
    fill(tempMatrix)
#    print("iniX: ",x," iniY: ",y)
#    print("meta:(",xMeta,yMeta,")")
    while x!=xMeta or y!=yMeta:
        if x<xMeta:
            x+=5
        elif x>xMeta:
            x-=5
            
        if y<yMeta:
            y+=5
        elif y>yMeta:
            y-=5
        printMatrix()
        fill(tempMatrix)
        if(y<525):
            gameDisplay.blit(sprite,(x+7,y+7))
        else:
            gameDisplay.blit(sprite,(x,y))
        pygame.display.update()
        clock.tick(60)
        count+=1
        
def printM(matrix):
    for i in matrix:
        for j in i:
            if j=="":
                print("0", end=" ")
            else:
                print("1",end=" ")
        print()


def spriteName(sprite):
    if sprite==negReyImg:
        return "NR"
    elif sprite==blaReyImg:
        return "BR"
    elif sprite==negTorImg:
        return "NT"
    elif  sprite==blaTorImg:
        return "BT"
    elif sprite==negCabImg:
        return "NC"
    elif sprite==blaCabImg:
        return "BC"
    elif sprite==negAlfImg:
        return "NA"
    elif sprite==blaAlfImg:
        return "BA"
    elif sprite==negDamImg:
        return "ND"
    elif sprite==blaDamImg:
        return "BD"
    elif sprite==negPeoImg:
        return "NP"
    elif sprite==blaPeoImg:
        return "BP"
    else:
        return ""
"""
ciclo de ejecucion
"""
def execute():
    global spritesMatrix,piecesMatrix,whitePlayer,movesCount
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
            coorX=roundBy75(pygame.mouse.get_pos()[0])
            coorY=roundBy75(pygame.mouse.get_pos()[1])
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
                                    catchSound.play()
                                    catched=True
                            else:
                                if(sprite in blackPieces):
                                    catchSound.play()
                                    catched=True                                
                    else:
                        
                        if(rules.IsLegalMove(piece,piecesMatrix,(iniPosI,iniPosJ),(loc[0],loc[1]))):
                            spritesMatrix[iniPosI][iniPosJ]=""
                            piecesMatrix[iniPosI][iniPosJ]=""
                            moveAnimation(sprite,iniX,iniY,coorX,coorY,spritesMatrix)
                            spritesMatrix[loc[0]][loc[1]]=sprite
                            piecesMatrix[loc[0]][loc[1]]=piece
                            strMove = str(movesCount)+". "+piece+"  "+converIndCol(iniPosJ)+":"+converIndFil(iniPosI)+" -> "+converIndCol(loc[1])+":"+converIndFil(loc[0])
                            printMessage(strMove)
                            movesCount+=1
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
