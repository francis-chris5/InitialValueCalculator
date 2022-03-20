# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:41:04 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import math


class IVP():
    def __init__(self, time=0, function=1, deltaTime=0.1):
        self.time = time
        self.function = function
        self.deltaTime = deltaTime
        
        
        
    def setFunction(self, function):
        if "," in function:
            self.function = function.split(",")
            print(self.function)
            for i in range(len(self.function)):
                self.function[i] = float(self.function[i].strip())
            print(self.function)
            self.solve(self.function)
            
        else:
            self.function = function
            print(self.function)
            for t in range(10):
                self.solve(t)
            
        
    def solve(self, t):
        if isinstance(self.function, list):
            for t in range(len(self.function)):
                print(self.function[t])
        else:
            print(eval(self.function))
        
        
        
    def __str__(self):
        bigCurly = "\\Bigg\\{"
        block = "\\begin{align*} u'(t) = " + str(self.function) + " \\\\ u(" + str(self.time) + ") \\\\ " + "\\end{align*}"
        result = bigCurly + " " + block
        return result
        
        