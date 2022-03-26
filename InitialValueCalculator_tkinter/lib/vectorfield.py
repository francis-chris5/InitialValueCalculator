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

##
# The VectorField object is a plotting surface for a initial value problem solved using Euler's Method and the exact solution for comparison
class VectorField(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.wide = int(float(self["width"]) / 2)
        self.tall = int(float(self["height"]) / 2)
        self.xScale = 1
        self.yScale = 1
        self.showAxis()
        
        
    def setScale(self, xRange, yRange):
        if abs(0 - xRange[0]) > abs(0 - xRange[1]):
            self.xScale = self.wide / xRange[0]
        else:
            self.xScale = self.wide / xRange[1]
            
        if abs(0 - yRange[0]) > abs(0 - yRange[1]):
            self.yScale = self.tall / yRange[0]
        else:
            self.yScale = self.tall / yRange[1]
            

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
        ## each plot draws an error of length deltaT
        i = a*self.wide + self.wide
        previous = i-1
        while i < b*self.wide+self.wide:
            self.create_arrow(previous, int(self["height"]) - self.tall*squareFunction(previous/self.wide), i, int(self["height"]) - self.tall*squareFunction(i/self.wide))          
            previous = i
            i += self.deltaX*self.wide
            
            
            
    def create_arrow(self, a=0, b=0, c=1, d=1):
        a = a * self.xScale + self.wide
        b = b * self.yScale + self.tall
        c = c * self.xScale + self.wide
        d = d * self.yScale + self.tall
        x = (c - a)
        y = (d - b)
        magnitude = math.sqrt(x**2 + y **2)
        angle = math.atan(y / x)
        self.create_line(a, b, c, d, width=4)
        self.create_line(c, d, c+10*math.sin(angle-math.pi/6), d-10*math.cos(angle-math.pi/6), width=2)
        self.create_line(c, d, c-10*math.sin(angle+math.pi/6), d+10*math.cos(angle+math.pi/6), width=2)
        
    def create_curve(self, a=0, b=0, c=1, d=1):
        a = a * self.xScale + self.wide
        b = b * self.yScale + self.tall
        c = c * self.xScale + self.wide
        d = d * self.yScale + self.tall
        self.create_line(a, b, c, d, width=3, fill="red")
        
































###################################  WHITE SPACE FOR SCROLLING  ################################