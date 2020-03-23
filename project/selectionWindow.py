from tkinter import * 
from tkinter.ttk import *

class selectionWindow():
    
    def __init__(self, main_window):
        self.negTorImg = PhotoImage(file = "images//NT.png")
        self.negTorImg = resizeImg(self.negTorImg,'T')
        self.blaTorImg = PhotoImage(file = "images//BT.png")
        self.blaTorImg = resizeImg(self.blaTorImg,'T')
        self.negCabImg = PhotoImage(file = "images//NC.png")
        self.negCabImg = resizeImg(self.negCabImg,'C')
        self.blaCabImg = PhotoImage(file = "images//BC.png")
        self.blaCabImg = resizeImg(self.blaCabImg,'C')
        self.negAlfImg = PhotoImage(file = "images//NA.png")
        self.negAlfImg = resizeImg(self.negAlfImg,'A')
        self.blaAlfImg = PhotoImage(file = "images//BA.png")
        self.blaAlfImg = resizeImg(self.blaAlfImg,'A')
        self.negDamImg = PhotoImage(file = "images//ND.png")
        self.negDamImg = resizeImg(self.negDamImg,'D')
        self.blaDamImg = PhotoImage(file = "images//BD.png")
        self.blaDamImg = resizeImg(self.blaDamImg,'D')
        main_window.title("Seleccione una pieza")
        self.root = main_window
        self.name =""
        
        
    def setItems(self,items):
        for i in range(len(items)):
            tempImg = self.getImg(items[i])
            Button(self.root, text=items[i] , image = tempImg,command=lambda pName =items[i]: self.onSelect(pName)).grid(row=0, column=i)
        
    def onSelect(self,pieceName):
        self.name = pieceName
        self.root.destroy()
        

        
    def getImg(self,name):
        if name=="NR":
            return self.negReyImg
        elif name=="BR":
            return self.blaReyImg
        elif name=="NT":
            return self.negTorImg
        elif  name=="BT":
            return self.blaTorImg
        elif name=="NC":
            return self.negCabImg
        elif name=="BC":
            return  self.blaCabImg
        elif name=="NA" :
            return self.negAlfImg
        elif name=="BA":
            return  self.blaAlfImg
        elif name=="ND" :
            return self.negDamImg
        elif name=="BD":
            return self.blaDamImg
        elif name=="NP":
            return self.negPeoImg
        elif name=="BP":
            return self.blaPeoImg
        else:
            return ""
        
def resizeImg(img,typ):
    if ('A' in typ):
        return img.subsample(14, 14) 
    if ('C' in typ):
        return img.subsample(16,16)
    if ('D' in typ):
        return img.subsample(12, 12)
    else:
        return img.subsample(3, 3)
        
