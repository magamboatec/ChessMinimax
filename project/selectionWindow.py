import tkinter as tk
from tkinter import ttk
class selectionWindow(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Lista en Tcl/Tk")
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
        

        


