# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:11:17 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import tkinter as tk
import math

def squareFunction(x):
    return x ** 2

class VectorField(tk.Canvas):
    def __init__(self, parent, function=squareFunction, deltaX=0.1, ticks=10, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.function = function
        self.deltaX = deltaX
        self.ticks = ticks
        self.wide = int(float(self["width"]) / self.ticks)
        self.tall = int(float(self["height"]) / self.ticks)
        self.showAxis()
        
        
        
    def showAxis(self):
            ## horizontal axis
        self.create_line(0, float(self["height"])/2, float(self["width"]), float(self["height"])/2, fill="blue", width=2) 
        # for i in range(self.wide, (self.ticks-1) * self.wide, self.tall):
        #     self.create_line(i, float(self["height"])/2 - 5, i, float(self["height"])/2 + 5, fill="blue", width = 2)
            
            ## vertical axis
        self.create_line(float(self["width"])/2, 0, float(self["width"])/2, float(self["height"]), fill="blue", width=2)
        # for i in range(0, int(float(self["height"]) - 3* self.tall), self.tall):
        #     self.create_line(self.wide-5, i, self.wide+5, i, fill="blue", width = 2)
        
        

    def plot(self, a=1, b=1):
        ## max value needs to be forty-five percent of plot area
        i = a*self.wide + self.wide
        previous = i-1
        while i < b*self.wide+self.wide:
            self.create_arrow(previous, int(self["height"]) - self.tall*squareFunction(previous/self.wide), i, int(self["height"]) - self.tall*squareFunction(i/self.wide))
            
            previous = i
            i += self.deltaX*self.wide
            
            
            
    def create_arrow(self, a=0, b=0, c=1, d=1):
        x = c - a
        y = d - b
        magnitude = math.sqrt(x**2 + y **2)
        angle = math.atan(y / x)
        self.create_line(a, b, c, d, width=4)
        self.create_line(c, d, c+10*math.sin(angle-math.pi/6), d-10*math.cos(angle-math.pi/6), width=2)
        self.create_line(c, d, c-10*math.sin(angle+math.pi/6), d+10*math.cos(angle+math.pi/6), width=2)
        