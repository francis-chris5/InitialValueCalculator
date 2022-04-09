# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 10:37:55 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""


import tkinter as tk


##
# Object to format the set of values in the solution nicely for output
class Table(tk.Frame):
    
    ##
    # Constructor
    # @param parent -the tk widget which will be the parent of this object
    # @param rows -the 2-dimensional set/list/tuple of solutions
    # @param title -the label to put on this table
    def __init__(self, parent, rows, title, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.rows = rows
        self.title = title
        self.header = ["t", "u(t)", "v(t)"]
        self.deltaT = 0.1
        self.layout()
        
        
        
        
    ##
    # Method to load the data into the table. When ready set the rows attribute to the desired solutions list and then call this method
    def layout(self):
        titleRow = tk.Label(self, text=str(self.title), border=3, relief="raised", bg="#343434", fg="#d1d1d1")
        headerT = tk.Label(self, text=str(self.header[0]), border=2, relief="raised", bg="#343434", fg="#d1d1d1")
        headerU = tk.Label(self, text=str(self.header[1]), border=2, relief="raised", bg="#343434", fg="#d1d1d1")
        headerV = tk.Label(self, text=str(self.header[2]), border=2, relief="raised", bg="#343434", fg="#d1d1d1")
        titleRow.grid(row=0, column=0, columnspan=3, sticky="EW")
        headerT.grid(row=1, column=0, sticky="EW")
        headerU.grid(row=1, column=1, sticky="EW")
        headerV.grid(row=1, column=2, sticky="EW")
        if isinstance(self.rows[0], list):
            for i, r in enumerate(self.rows):
                r.insert(0, i * self.deltaT)
            for i,r in enumerate(self.rows):
                for j,c in enumerate(r):
                    cell = tk.Label(self, text=str(c), border=1, relief="raised")
                    cell.grid(row=i+2, column=j, sticky="EW")
        else:
            for i, r in enumerate(self.rows):
                time = tk.Label(self, text=str(i * self.deltaT), border=1, relief="raised")
                time.grid(row=i+2, column=0, sticky="EW")
                cell = tk.Label(self, text=str(r), border=1, relief="raised")
                cell.grid(row=i+2, column=1, sticky="EW")

                
                
                
    def clear(self):
        tableCells = self.winfo_children()
        for tc in tableCells:
            tc.destroy()
            
            