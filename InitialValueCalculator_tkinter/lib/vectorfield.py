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
# The VectorField object is a plotting surface for a initial value problem solved using Euler's Method (in black) and the exact solution (in red) for comparison.
class VectorField(tk.Canvas):
    
    ##
    # Constructor
    # @param parent -the tk widget to serve as the parent of this widget
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.wide = int(float(self["width"]) / 2)
        self.tall = int(float(self["height"]) / 2)
        self.xScale = 1
        self.yScale = 1
        self.showAxis()
        
        
    ##
    # Method to set the ratio of number of pixels to an interval in the domain/range of the function.
    # @param xRange -a 2-dimensional list/tuple with the minimum (index 0) and the maximum (index 1) values to be plotted in the domain
    # @param yRange -a 2-dimensional list/tuple with the minimum (index 0) and the maximum (index 1) values to be plotted in the range
    def setScale(self, xRange, yRange):
        if abs(0 - xRange[0]) > abs(0 - xRange[1]):
            self.xScale = self.wide / xRange[0]
        else:
            self.xScale = self.wide / xRange[1]
            
        if abs(0 - yRange[0]) > abs(0 - yRange[1]):
            self.yScale = self.tall / yRange[0]
        else:
            self.yScale = self.tall / yRange[1]
            


    ##
    # Method to plot the x-axis and y-axis on the surface for reference (tick marks with scale are near the top of the list of features to be left off under time constraints)
    def showAxis(self):
            ## horizontal axis
        self.create_line(0, float(self["height"])/2, float(self["width"]), float(self["height"])/2, fill="blue", width=2) 
            
            ## vertical axis
        self.create_line(float(self["width"])/2, 0, float(self["width"])/2, float(self["height"]), fill="blue", width=2)
        
        

    # ##
    # # if time allows move the looping through solutions inside the object here
    # def plot(self, a=1, b=1):
    #     ## max value needs to be forty-five percent of plot area
    #     ## each plot draws an error of length deltaT
    #     i = a*self.wide + self.wide
    #     previous = i-1
    #     while i < b*self.wide+self.wide:
    #         self.create_arrow(previous, int(self["height"]) - self.tall*squareFunction(previous/self.wide), i, int(self["height"]) - self.tall*squareFunction(i/self.wide))          
    #         previous = i
    #         i += self.deltaX*self.wide
            
            
      
    ##
    # Method to plot a single arrow on the vector field. Call this repeatedly to plot the entire solution. Hopefully this will be updated for vector like coordinates (two lists) before due date.
    # @param a -starting x coordinate
    # @param b -starting y coordinate
    # @param c -ending x coordinate
    # @param d -ending y coordinate
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
        
        
    ##
    # Method to plot a single line segment on the vector field. Call this repeatedly to plot the entire exact solution with the end point always one pixel over (domain) from the start point. Hopefully this will be updated for vector like coordinates (two lists) before due date.
    # @param a -starting x coordinate
    # @param b -starting y coordinate
    # @param c -ending x coordinate
    # @param d -ending y coordinate
    def create_curve(self, a=0, b=0, c=1, d=1):
        a = a * self.xScale + self.wide
        b = b * self.yScale + self.tall
        c = c * self.xScale + self.wide
        d = d * self.yScale + self.tall
        self.create_line(a, b, c, d, width=3, fill="red")
        
































###################################  WHITE SPACE FOR SCROLLING  ################################