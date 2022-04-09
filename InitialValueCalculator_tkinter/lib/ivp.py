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
     
    
    

    ##
    # This method is the one to actually go through the exact solution for comparitive purposes
    # @param function -string representing the time dependent differential function to be solved, delimit vector dimensions for the function with an ampersand (&)
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
        self.u = ["u", "v"]
        self.xRange = [-1, 1]
        self.yRange = [-1, 1]
        
        
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
    # (I don't think this is part of Euler's method) determines solution to the differential to use in the calculation, if entered directly it uses that, solving a number of cases may be attempted but time requirements for class project may prevent that
    # @param u -string representing the solution or set of solutions to the differential equation
    def setSolutionFunctions(self, u):
        if "," in u:
            self.u = u.spli(",")
            ## discrete set, put this in if time allows
        elif "&" in u:
            self.u = u.split("&")
        else:
            self.u = u
        print(self.u)
            
            
    ##
    # Method that actually steps through the function starting with the initial values provided and finds the next estimated point by using Euler's Method.
    # @param differential -string from the input field representing the initial value(s). Use an ampersand (&) to delimit a piecewise vector function
    def solve(self, differential):
        if "&" in differential:
            """
            SUBMISSION COMMENT: This is the walking through Euler's Method portion for Vector Inputs
                1.) split the vector into components
                2.) walk through the appropriate number of steps
                3.) calculate the solutions for each dimension and append to the list of discrete time solutions
                4.) the else block below repeats steps for one dimensional function
            """
            #differential = differential.replace("u", self.u[0]) ##this is more of the RK stuff, didn't want to delete it for future updates on this app seems worth pursueing
            #differential = differential.replace("v", self.u[1])
            self.differential = differential.split("&")
            currentStep = 1
            t = 0
            while currentStep <= self.steps:
                u = self.functionU[currentStep-1][0]
                v = self.functionU[currentStep-1][1]
                t += self.deltaT
                self.functionU.append([u + self.deltaT * eval(self.differential[0]), v + self.deltaT * eval(self.differential[1])])
                currentStep += 1
                ##UPDATE: for dimension in self.funtion[currentStep-1]: #calculate each dimension, append to step-list, then append step-list to full list afterwards ##this would work for simple 2d case of u and t as well
        else:
            #differential = differential.replace("u", self.u)
            self.differential = differential 
            currentStep = 1
            t = 0
            while currentStep <= self.steps:
                u = self.functionU[currentStep-1]
                t += self.deltaT
                self.functionU.append(self.functionU[currentStep-1] + self.deltaT * eval(self.differential))
                currentStep += 1
                
    
    ##
    # Method to find the minimum/maximum values for x and y corrdinates to set scale on the plot area
    def minMax(self):
        if isinstance(self.functionU[0], list):
            for x in self.functionU[0]:
                minimum = self.functionU[0][0]
                maximum = self.functionU[0][0]
                if x < minimum:
                    minimum = x
                if x > maximum:
                    maximum = x
            xMin = minimum
            xMax = maximum
            for y in self.functionU[1]:
                minimum = self.functionU[0][0]
                maximum = self.functionU[0][0]
                if y < minimum:
                    minimum = y
                if y > maximum:
                    maximum = y
            yMin = minimum
            yMax = maximum
            self.xRange = [xMin, xMax]
            self.yRange = [yMin, yMax]
        else:
            i = 1
            time = [0]
            while i < len(self.functionU):
                time.append(time[i-1]+self.deltaT)
                i += 1
            self.xRange = [min(time), max(time)]
            self.yRange = [min(self.functionU), max(self.functionU)]
                

        
        
        
    def __str__(self):
        return str(self.differential)
































###########################  WHITE SPACE FOR SCROLLING  ##########################        
        