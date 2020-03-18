import pygame
from Rules import Rules
from ScrollingTextBox import ScrollingTextBox
from fileManager import FileManager
from AI import AI
from selectionWindow import selectionWindow
import datetime
import tkinter as tk
from tkinter import ttk
from math import inf

pygame.init()
pygame.mixer.init()
music=pygame.mixer.music.load("sounds//file.mp3")
catchSound=pygame.mixer.Sound("sounds//catch.wav")
pygame.mixer.music.set_volume(0.1)
catchSound.set_volume(0.2)
pygame.mixer.music.play(-1)

blackColor = (0,0,0)
gameDisplay = pygame.display.set_mode((1200,760),0,32)
pygame.display.set_caption("Chess solver")
gameDisplay.fill((0,0,0))
clock = pygame.time.Clock()
rules = Rules()

playerMove = True
AIColor = "Negro"

negReyImg = pygame.transform.scale(pygame.image.load("images//NR.png"),(75,75))
blaReyImg = pygame.transform.scale(pygame.image.load("images//BR.png"),(75,75))
negTorImg = pygame.transform.scale(pygame.image.load("images//NT.png"),(55,55))
blaTorImg = pygame.transform.scale(pygame.image.load("images//BT.png"),(55,55))
negCabImg = pygame.transform.scale(pygame.image.load("images//NC.png"),(60,60))
blaCabImg = pygame.transform.scale(pygame.image.load("images//BC.png"),(60,60))
negAlfImg = pygame.transform.scale(pygame.image.load("images//NA.png"),(65,65))
blaAlfImg = pygame.transform.scale(pygame.image.load("images//BA.png"),(65,65))
negDamImg = pygame.transform.scale(pygame.image.load("images//ND.png"),(68,68))
blaDamImg = pygame.transform.scale(pygame.image.load("images//BD.png"),(68,68))
negPeoImg = pygame.transform.scale(pygame.image.load("images//NP.png"),(50,50))
blaPeoImg = pygame.transform.scale(pygame.image.load("images//BP.png"),(50,50))
brownSquare = pygame.transform.scale(pygame.image.load("images//brown_square.jpg"),(75,75))
whiteSquare = pygame.transform.scale(pygame.image.load("images//white_square.jpg"),(75,75))
cyanSquare = pygame.transform.scale(pygame.image.load("images//blue_square.jpg"),(75,75))
bordeImg = pygame.transform.scale(pygame.image.load("images//borde.png"),(690,690))
fondoImg = pygame.image.load("images//fondo.jpg")
paperSheetImg = pygame.transform.scale(pygame.image.load("images//paperSheet.png"),(int(423*1.2),int(595*1.2)))
plumaImg = pygame.image.load("images//pluma.png")

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

missedPiecesPlayer = []
missedPiecesAI = []

gameDisplay.blit(fondoImg,(0,0))
gameDisplay.blit(bordeImg,(30,30))
boardSurface = gameDisplay.blit(paperSheetImg,(800,0))
gameDisplay.blit(plumaImg,(990,150))


log = ""
movesCount=1

class resurrectedPiece:
    def _init_(self):
        self.name=""

def drawMessage(message):
  
    #prints a string to the area to the right of the board
    textBox.Add(message)
    textBox.Draw()

    
textBox = ScrollingTextBox(gameDisplay,860,1100,40,670)

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
    white = (250, 250, 250)
    markersA = ["a","b","c","d","e","f","g","h"]
    markersB = ["8","7","6","5","4","3","2","1"]
    x=39
    y=40
    font = pygame.font.Font('freesansbold.ttf', 30)
    for i in markersA:
        x+=75
        text = font.render(i, True, white)
        textRect = text.get_rect()
        textRect.center = (x,737)
        gameDisplay.blit(text, textRect)
    for i in markersB:
        y+=75
        text = font.render(i, True, white)
        textRect = text.get_rect()
        textRect.center = (20,y)
        gameDisplay.blit(text, textRect)        
    
drawMarkets()
#Imprime el tablero de juego
def drawMatrix():
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
            sprite=spritesMatrix[fil][col]
            pos = gameMatrix[fil][col]
            piece = piecesMatrix[fil][col]
            if sprite!="":
                if('P' in piece):
                    gameDisplay.blit(sprite,(pos[0]+12,pos[1]+25))
                elif('D' in piece):    
                    gameDisplay.blit(sprite,(pos[0]+5,pos[1]+7))
                elif('A' in piece): 
                    gameDisplay.blit(sprite,(pos[0]+6,pos[1]+10))
                elif('C' in piece): 
                    gameDisplay.blit(sprite,(pos[0]+8,pos[1]+15))
                elif('T' in piece): 
                    gameDisplay.blit(sprite,(pos[0]+10,pos[1]+20))
                    
                else:
                    gameDisplay.blit(sprite,pos)
      
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
    while x!=xMeta or y!=yMeta:
        if x<xMeta:
            x+=5
        elif x>xMeta:
            x-=5
            
        if y<yMeta:
            y+=5
        elif y>yMeta:
            y-=5
        drawMatrix()
        fill(tempMatrix)
        if(y<570):
            gameDisplay.blit(sprite,(x+10,y+10))
        else:
            gameDisplay.blit(sprite,(x+5,y+5))
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

def locate(matrix):
    global piecesMatrix
    piecesMatrix=matrix
    sprite = ""
    for i in range(8):
        for j in range(8):
            if piecesMatrix[i][j]=="NR":
                sprite=negReyImg
            elif piecesMatrix[i][j]=="BR":
                sprite=blaReyImg
            elif piecesMatrix[i][j]=="NT":
                sprite=negTorImg
            elif piecesMatrix[i][j]=="BT":
                sprite=blaTorImg
            elif piecesMatrix[i][j]=="NC":
                sprite=negCabImg
            elif piecesMatrix[i][j]=="BC":
                sprite=blaCabImg
            elif piecesMatrix[i][j]=="NA":
                sprite=negAlfImg
            elif piecesMatrix[i][j]=="BA":
                sprite=blaAlfImg
            elif piecesMatrix[i][j]=="ND":
                sprite=negDamImg
            elif piecesMatrix[i][j]=="BD":
                sprite=blaDamImg
            elif piecesMatrix[i][j]=="NP":
                sprite=negPeoImg
            elif piecesMatrix[i][j]=="BP":
                sprite=blaPeoImg
            else:
                sprite=""
            spritesMatrix[i][j]=sprite
def copyMatrix(matrix):
    newMatrix=[]
    for i in matrix:
        newMatrix.append(i[:])
    return newMatrix    
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
def getSprite(name):
    if name=="NR":
        return negReyImg
    elif name=="BR":
        return blaReyImg
    elif name=="NT":
        return negTorImg
    elif  name=="BT":
        return blaTorImg
    elif name=="NC":
        return negCabImg
    elif name=="BC":
        return  blaCabImg
    elif name=="NA" :
        return negAlfImg
    elif name=="BA":
        return  blaAlfImg
    elif name=="ND" :
        return negDamImg
    elif name=="BD":
        return blaDamImg
    elif name=="NP":
        return negPeoImg
    elif name=="BP":
        return blaPeoImg
    else:
        return ""
def drawInfo(endGame,winnerColor):
    gameDisplay.blit(paperSheetImg,(800,0))
    gameDisplay.blit(plumaImg,(990,150))
    font = pygame.font.Font('freesansbold.ttf', 15)    
    text = font.render("Color Jug: "+playerColor, 1, (20, 20, 20))
    gameDisplay.blit(text, (1050,45))
    text = font.render("Color AI: "+AIColor, 1, (20, 20, 20))
    gameDisplay.blit(text, (1050,65))
    if(endGame):
        text = font.render("Jaque Mate!!", 1, (20, 20, 20))
        gameDisplay.blit(text, (1050,110))         
        text = font.render("Ganador: "+winnerColor, 1, (20, 20, 20))
        gameDisplay.blit(text, (1050,130))        
    elif playerMove:
        text = font.render("Juega: "+playerColor, 1, (20, 20, 20))
        gameDisplay.blit(text, (1050,110))
    else:
        text = font.render("Juega:"+AIColor, 1, (20, 20, 20))
        gameDisplay.blit(text, (1050,110))

       
"""
ciclo de ejecucion
"""
def execute():
    global spritesMatrix,piecesMatrix,playerMove,movesCount,log,playerColor,AIColor,missedPiecesPlayer,missedPiecesAI
    catched= False #permite saber si ya ha elegido una pieza
    sprite=""
    piece =""
    done = False
    endGame =False
    winnerColor=""
    iniX =0
    iniY =0
    iniPosI=0
    iniPosJ=0
    iniMatrix=FileManager.getMatrix()
    locate(iniMatrix)
    startCol=FileManager.getStartColor()
    AICol=FileManager.getAIColor()
    inteligence = AI()
    if(AICol==startCol):
        playerMove=False
    else:
        playerMove=True
        
    if(('B' in AICol) or ('b' in AICol) or ('w' in AICol)or ('W' in AICol)):
        AIColor="Blanco"
        playerColor="Negro"
    else:
        AIColor="Negro"
        playerColor="Blanco"
    missedPiecesAI=FileManager.getMissedPieces(iniMatrix,AIColor)
    missedPiecesPlayer=FileManager.getMissedPieces(iniMatrix,playerColor)
    drawInfo(endGame,winnerColor)
    textBox.Draw()
    isMusicPlaying=True
    while not done:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if(event.key==27):
                    done = True
                elif(event.key==109 or event.key==32):
                    if(isMusicPlaying):
                        pygame.mixer.music.stop()
                        isMusicPlaying=False
                    else:
                        pygame.mixer.music.play(-1)
                        isMusicPlaying=True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if(event.button== 4):
                    if(boardSurface.collidepoint(pygame.mouse.get_pos())):
                        textBox.MoveUp()
                        drawInfo(endGame,winnerColor)
                        textBox.Draw()
                        
                if(event.button==5):
                    if(boardSurface.collidepoint(pygame.mouse.get_pos())):
                        textBox.MoveDown()
                        drawInfo(endGame,winnerColor)
                        textBox.Draw()
                    
                if(event.button == 3):
                    catched= False
                coorX=roundBy75(pygame.mouse.get_pos()[0])
                coorY=roundBy75(pygame.mouse.get_pos()[1])
                loc=buscarIndice(coorX,coorY)
                if(event.button == 1 and playerMove and loc!=(-1,-1) and not(endGame)):
                    if(not catched):   
                        iniPosI=loc[0]
                        iniPosJ=loc[1]
                        iniX = coorX
                        iniY = coorY
                        sprite= spritesMatrix[loc[0]][loc[1]]
                        piece = piecesMatrix[loc[0]][loc[1]]
                        if((sprite in whitePieces )and ('B' in playerColor) and (sprite!="")):
                            catchSound.play()
                            catched=True
                        elif((sprite in blackPieces )and ('N' in playerColor) and (sprite!="")):
                            catchSound.play()
                            catched=True                               
                    else:
                        if(rules.IsLegalMove(piece,piecesMatrix,(iniPosI,iniPosJ),(loc[0],loc[1])) and not(rules.DoesMovePutPlayerInCheck(piecesMatrix,playerColor,(iniPosI,iniPosJ),(loc[0],loc[1])))):   
                            spritesMatrix[iniPosI][iniPosJ]=""
                            piecesMatrix[iniPosI][iniPosJ]=""
                            if(AIColor[0] in piecesMatrix[loc[0]][loc[1]] and not('P' in piecesMatrix[loc[0]][loc[1]])):
                                missedPiecesAI.append(piecesMatrix[loc[0]][loc[1]])
                            moveAnimation(sprite,iniX,iniY,coorX,coorY,spritesMatrix)
                            spritesMatrix[loc[0]][loc[1]]=sprite
                            piecesMatrix[loc[0]][loc[1]]=piece
                            strMove = str(movesCount)+". "+piece+"  "+converIndCol(iniPosJ)+":"+converIndFil(iniPosI)+" -> "+converIndCol(loc[1])+":"+converIndFil(loc[0])
                            log += strMove+"\n"
                            
                            
                            iniX = 0
                            iniY = 0
                            iniPosI=0
                            iniPosJ=0
                            catched=False                              
                            playerMove=not playerMove
                            drawInfo(endGame,winnerColor)
                            drawMessage(strMove)
                            
                            if("BP" == piece and loc[0]==0 ) or ("NP" == piece and loc[0]==7 ) :
                                main_window = tk.Tk()
                                app = selectionWindow(main_window)
                                app.setItems(missedPiecesPlayer)
                                app.mainloop()
                                
                                if(app.name!=""):
                                    spritesMatrix[loc[0]][loc[1]]=getSprite(app.name)
                                    piecesMatrix[loc[0]][loc[1]]=app.name
                                    missedPiecesPlayer.remove(app.name)
                            movesCount+=1                

                                        
            #--- computer move
            if(not playerMove and not endGame):

                move = inteligence.play(piecesMatrix,AIColor)
                
                if move[2]==-inf:
                    winnerColor=playerColor
                    endGame = True
                    drawInfo(endGame,winnerColor)
                    textBox.Draw()                    
                    
                else:    
                    iniPos = move[0]
                    finPos = move[1]
                    sprite = spritesMatrix[iniPos[0]][iniPos[1]]
                    piece = piecesMatrix[iniPos[0]][iniPos[1]]
                    iniCoord = gameMatrix[iniPos[0]][iniPos[1]]
                    finCoord = gameMatrix[finPos[0]][finPos[1]]

                    spritesMatrix[iniPos[0]][iniPos[1]]=""
                    piecesMatrix[iniPos[0]][iniPos[1]]=""                    
                    if(playerColor[0] in piecesMatrix[finPos[0]][finPos[1]] and not('P' in piecesMatrix[finPos[0]][finPos[1]])):
                        missedPiecesPlayer.append(piecesMatrix[finPos[0]][finPos[1]])                                    
                    moveAnimation(sprite,iniCoord[0],iniCoord[1],finCoord[0],finCoord[1],spritesMatrix)
                    spritesMatrix[finPos[0]][finPos[1]]=sprite
                    piecesMatrix[finPos[0]][finPos[1]]=piece
                    if("BP" == piece and finPos[0]==0 ) or ("NP" == piece and finPos[0]==7):
                        pieceName=inteligence.getMaxMissedPiece(missedPiecesAI)
                        spritesMatrix[finPos[0]][finPos[1]]=getSprite(pieceName)
                        piecesMatrix[finPos[0]][finPos[1]]=pieceName
                        missedPiecesAI.remove(pieceName)
                    strMove = str(movesCount)+". "+piece+"  "+converIndCol(iniPos[1])+":"+converIndFil(iniPos[0])+" -> "+converIndCol(finPos[1])+":"+converIndFil(finPos[0])
                    log += strMove+"\n"
                    
                    playerMove=not playerMove
                    drawInfo(endGame,winnerColor)
                    drawMessage(strMove)
                    movesCount+=1
            if(rules.IsCheckmate(piecesMatrix,playerColor)):
                    winnerColor=AIColor
                    endGame = True
                    drawInfo(endGame,winnerColor)
                    textBox.Draw() 
                
                
                            


                            
 
        drawMatrix()
        if(catched):
            gameDisplay.blit(cyanSquare,(iniX,iniY));
            
        fill(spritesMatrix)


        
        pygame.display.update()
        clock.tick(30)
    time = datetime.datetime.now()
    strOutput="Partida: "+str(time)+"\nAI: "+AIColor+"\nJugador: "+playerColor+"\n***********************\n"+log
    fileName ="matches//"+str(time).replace(":",".")+".txt"
    FileManager.save(fileName,strOutput)
    pygame.quit()    
execute()

