# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 08:41:12 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import tkinter as tk
import tkinter.ttk as ttk


class ScrollFrame(tk.Frame):
    
    ##
    # Constructor
    # @param parent -the tk widget which this widget will be loaded into
    # @param info -the string to load onto the dialog box (probably the contents of a text file with help or about information)
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.cvsMain = tk.Canvas(self)
        self.frmContent = ttk.Frame(self.cvsMain)
        self.scrVertical = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.cvsMain.yview)
        
        self.frmContent.bind("<Configure>", lambda event: self.cvsMain.configure(scrollregion=self.cvsMain.bbox("all")))
        self.cvsMain.create_window((0,0), window=self.frmContent, anchor="nw")
        self.cvsMain.configure(yscrollcommand=self.scrVertical.set)

        self.cvsMain.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.scrVertical.pack(fill="y", side="right")
        
        
    