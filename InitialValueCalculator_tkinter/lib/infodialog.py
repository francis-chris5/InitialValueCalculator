# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:10:30 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import tkinter as tk
import tkinter.ttk as ttk

class InfoDialog(tk.Frame):
    def __init__(self, parent, info, width=432, height=345, *args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.info = info
        self.cvsMain = tk.Canvas(self)
        self.frmContent = ttk.Frame(self.cvsMain)
        self.scrVertical = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.cvsMain.yview)
        
        self.frmContent.bind("<Configure>", lambda event: self.cvsMain.configure(scrollregion=self.cvsMain.bbox("all")))
        self.cvsMain.create_window((0,0), window=self.frmContent, anchor="nw")
        self.cvsMain.configure(yscrollcommand=self.scrVertical.set)
        
        
        self.lblInfo = tk.Label(self.frmContent, text=self.info, wraplength=width-60, justify=tk.LEFT)
        
        
        self.cvsMain.pack(fill="both", expand=True, padx=5, pady=5)
        self.lblInfo.pack(fill="both", expand=True, side="left", padx=15, pady=15)
        self.scrVertical.pack(fill="y", side="right")
        
        
    