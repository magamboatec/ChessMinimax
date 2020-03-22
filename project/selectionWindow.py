import tkinter as tk
from tkinter import ttk
import pygame
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

class selectionWindow(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Seleccione una pieza")
        self.root = main_window
        self.name ="" 
        self.listbox = tk.Listbox(self, name='lb')
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        self.listbox.pack()
        self.pack()
        
        
    def setItems(self,items):
        self.listbox.insert(0, *items)
        
    def onselect(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        self.name = w.get(index)
        self.root.destroy()
        

        


