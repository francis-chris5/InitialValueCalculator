# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:41:04 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import math


class Exact():
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
    

class EulerMethod():
    def __init__(self, differential=1, deltaT=0.1, steps=1, functionU=[]):
        self.differential = differential
        self.deltaT = deltaT
        self.steps = steps
        self.functionU = functionU
        # self.functionV = functionV
        
        
    def setDeltaT(self, deltaT):
        self.deltaT = float(deltaT)
        
    def setSteps(self, steps):
        self.steps = float(steps)
        
    def setInitialU(self, u0):
        if "&" in u0:
            u0 = u0.split("&")
            self.functionU.append([float(u0[0]), float(u0[1])])
        else:
            self.functionU.append(float(u0))
        

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

            
        
    def evaluate(self, t):
        if isinstance(self.function, list):
            for t in range(len(self.function)):
                print(self.function[t])
        else:
            return(eval(self.function))
        
        
        
    def __str__(self):
        return str(self.differential)
































###########################  WHITE SPACE FOR SCROLLING  ##########################        
        