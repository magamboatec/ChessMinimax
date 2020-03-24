from tkinter import * 
from tkinter.ttk import *

class endWindow():
    
    def __init__(self, main_window,texto):
        self.root = main_window
        self.root.title("juego terminado")
        frame = Frame(self.root, width=250, height=100)
        frame.pack_propagate(0)    
        frame.pack()
        lbl_1=Label(frame,text="Jaque Mate!!")
        lbl_1.config(font=("Courier", 18))
        lbl_1.pack()
        lbl_2=Label(frame,text=texto)
        lbl_2.config(font=("Courier", 14))
        lbl_2.pack()
        btn=Button(frame,text="Aceptar",style='TButton',command=self.onSelect).pack()

    def onSelect(self):
        self.root.destroy()
        
