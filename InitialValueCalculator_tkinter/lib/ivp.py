# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:41:04 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import math



##
# Object to handle the exact solution for comparative reasons.
class Exact():
    
    ##
    # Constructor
    def __init__(self):
        pass
        
        
    def setDeltaT(self, deltaT):
        self.deltaT = float(deltaT)
        
    def setSteps(self, steps):
        self.steps = float(steps)
        
    def setInitialValue(self, initial):
        if "&" in initial:
            initial = initial.split("&")
            self.solutions = [[float(initial[0]),float(initial[1])]]
        else:
            self.solutions =[float(initial)]
        
    

    def evaluateFunction(self, function):
        if "," in function:
            self.function = function.split(",")
            for i in range(len(self.function)):
                self.function[i] = float(self.function[i].strip())
            self.solve(self.function)
        elif "&" in function:
            self.function = function.split("&")
            currentStep = 1
            while currentStep < self.steps:
                t = currentStep * self.deltaT
                uv = [eval(self.function[0]), eval(self.function[1])]
                self.solutions.append(uv)
                currentStep += 1
        else:
            self.function = function
            currentStep = 1
            while currentStep < self.steps:
                t = currentStep * self.deltaT
                self.solutions.append(eval(self.function))
                currentStep += 1
                
                
                
    def __str__(self):
        return str(self.function)
    


##
# Object to handle the solution to the time dependent differential with Euler's Method
class EulerMethod():
    
    ##
    # Constructor
    def __init__(self):
        self.differential = 1
        self.deltaT = 0.1
        self.steps = 1
        self.functionU = []
        # self.functionV = functionV
        
        
    ##
    # Method to set the value representing the time interval in the solution.
    # @param deltaT -A string from the input field that can be cast into a floating point number
    def setDeltaT(self, deltaT):
        self.deltaT = float(deltaT)
        
    ##
    # Method to set the value representing the number of steps to be taken in the solution.
    # @param steps -A string from the input field that can be cast into an integer value
    def setSteps(self, steps):
        self.steps = int(steps)
        
    
    ##
    # Method to set the intial value for the IVP problem. 
    # @param u0 -string from the input field representing the initial value(s). Use an ampersand (&) to delimit the dimensions in the initial vector.
    def setInitialU(self, u0):
        if "&" in u0:
            u0 = u0.split("&")
            #self.functionU.append([float(u0[0]), float(u0[1])])
            vector = []
            for i in u0:
                vector.append(float(i))
            self.functionU.append(vector)
        else:
            self.functionU.append(float(u0))
        

    ##
    # Method that actually steps through the function starting with the initial values provided and finds the next estimated point by using Euler's Method.
    # @param differential -string from the input field representing the initial value(s). Use an ampersand (&) to delimit a piecewise vector function
    def solve(self, differential):
        if "&" in differential:
            self.differential = differential.split("&")
            currentStep = 1
            t = 0
            while currentStep <= self.steps:
                u = self.functionU[currentStep-1][0]
                v = self.functionU[currentStep-1][1]
                t += self.deltaT
                self.functionU.append([self.functionU[currentStep-1][0] + eval(self.differential[0]), v + self.functionU[currentStep-1][1] + eval(self.differential[1])])
                currentStep += 1
        else:
            self.differential = differential 
            currentStep = 1
            t = 0
            while currentStep <= self.steps:
                u = self.functionU[currentStep-1]
                t += self.deltaT
                self.functionU.append(self.functionU[currentStep-1] + eval(self.differential))
                currentStep += 1

            
        
    ##
    # Internal method to find each particular solution in the set.
    def evaluate(self, t):
        if isinstance(self.function, list):
            for t in range(len(self.function)):
                print(self.function[t])
        else:
            return(eval(self.function))
        
        
        
    def __str__(self):
        return str(self.differential)
































###########################  WHITE SPACE FOR SCROLLING  ##########################        
        