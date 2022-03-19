# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:41:04 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""



class IVP():
    def __init__(self, time=0, function=1, deltaTime=0.1):
        self.time = time
        self.function = function
        self.deltaTime = deltaTime
        
        
        
        
        
    def __str__(self):
        bigCurly = "\\Bigg\\{"
        block = "\\begin{align*} u'(t) = " + str(self.function) + " \\\\ u(" + str(self.time) + ") \\\\ " + "\\end{align*}"
        result = bigCurly + " " + block
        return result
        
        