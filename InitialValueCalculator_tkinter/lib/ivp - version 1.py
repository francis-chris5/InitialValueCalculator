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
        
    def setTargetT(self, targetT):
        self.targetT = float(targetT)
        
    def setInitialValue(self, initial):
        self.solutions =[float(initial)]
        
    
    
    def evaluateFunction(self, function):
        if "," in function:
            self.function = function.split(",")
            for i in range(len(self.function)):
                self.function[i] = float(self.function[i].strip())
            print(self.function)
            self.solve(self.function)
        else:
            self.function = function
            print(self.function)
            currentStep = 1
            while currentStep < self.targetT:
                t = currentStep * self.deltaT
                self.solutions.append(eval(self.function))
                currentStep += 1
            print(self.solutions)
                
                
                
    def __str__(self):
        bigCurly = "\\Bigg\\{"
        block = "\\begin{align*} u'(t) = " + str(self.function) + " \\\\ u(" + str(self.time) + ") \\\\ " + "\\end{align*}"
        result = bigCurly + " " + block
        return result
    

class EulerMethod():
    def __init__(self, differential=1, deltaT=0.1, targetT=1, functionU=[1], functionV=[1]):
        self.differential = differential
        self.deltaT = deltaT
        self.targetT = targetT
        self.functionU = functionU
        self.functionV = functionV
        
        
    def setDeltaT(self, deltaT):
        self.deltaT = float(deltaT)
        
    def setTargetT(self, targetT):
        self.targetT = float(targetT)
        
    def setInitialU(self, u0):
        self.functionU[0] = float(u0)
        
    def setInitialV(self, v0):
        self.functionV[0] = float(v0)

    def solve(self, differential):
        if "&" in differential:
            self.differential = differential.split("&")
            currentStep = 1
            while currentStep < self.targetT:
                u = self.functionU[currentStep-1]
                v = self.functionV[currentStep-1]
                t = currentStep * self.deltaT
                self.functionU.append(eval(self.differential[0]))
                self.functionV.append(eval(self.differential[1]))
                currentStep += 1
        else:
            self.differential = differential 
            currentStep = 1
            while currentStep < self.targetT:
                u = self.functionU[currentStep-1]
                t = currentStep * self.deltaT
                self.functionU.append(eval(self.differential))
                currentStep += 1
        print(self.differential)
        print(self.targetT)
        print(self.functionU)
        print(self.functionV)
            
        
    def evaluate(self, t):
        if isinstance(self.function, list):
            for t in range(len(self.function)):
                print(self.function[t])
        else:
            return(eval(self.function))
        
        
        
    def __str__(self):
        bigCurly = "\\Bigg\\{"
        block = "\\begin{align*} u'(t) = " + str(self.function) + " \\\\ u(" + str(self.time) + ") \\\\ " + "\\end{align*}"
        result = bigCurly + " " + block
        return result
        
        