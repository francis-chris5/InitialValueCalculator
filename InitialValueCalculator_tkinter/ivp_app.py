# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:36:14 2022

@author: Christopher S. Francis

@language: Python 3.10.2

@summary: This file is the Graphcial User Interface (GUI) for an Initial Value Problem calculator using Euler's Method to solve

@note: the lines that relate to the project are [156 - 185]** CHANGE THIS AT SUBMISSION: SolveIVP function, the bulk of the problem at hand is in the file ivp.py located in the lib folder.
"""

import tkinter as tk
import tkinter.filedialog
import lib.ivp as ivp
import lib.vectorfield as vf
import lib.infodialog as info
import lib.table as table


# u = ivp.Exact()
# diff = ivp.EulerMethod()

#######################################  Functions  ##########################

##
# Method to reset the GUI for a new solution to be entered.
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def NewSolution(event):
    txtDifferential.delete(0, tk.END)
    txtUInitial.delete(0, tk.END)
    txtDeltaT.delete(0, tk.END)
    txtNumberOfSteps.delete(0, tk.END)
    txtUFunction.delete(0, tk.END)
    txtDifferential.focus_set()
    UpdateLeftStatus("Status: New IVP...")
    UpdateMidStatus("")
    UpdateRightStatus("")
    lstIVPSolutions.clear()
    lstExactSolutions.clear()
    pltVectorField.clearPlots()
##end NewSolution()


##
# Method to retrieve a previously solved solution. The application files include a version of the Lorenz Attractor to demonstrate how to input differentials and exact solutions. NOTE: the save process only saves the text from the input fields, after opening a saved solution it is still necessary to click the "Solve IVP" button.
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def OpenSolution(event):
    ##should probably put a want to save dialog here
    inputs = []
    filepath = tk.filedialog.askopenfilename(defaultextension=".ivp", filetypes=(("IVP calculator", "*.ivp"),("All Files", "*.*") ))
    with open(filepath, "r") as fromFile:
        for line in fromFile:
            inputs.append(line.strip())
    txtDifferential.delete(0, tk.END)
    txtUInitial.delete(0, tk.END)
    txtDeltaT.delete(0, tk.END)
    txtNumberOfSteps.delete(0, tk.END)
    txtUFunction.delete(0, tk.END)
    lstIVPSolutions.clear()
    lstExactSolutions.clear()
    
    txtDifferential.insert(0,inputs[0])
    txtUInitial.insert(0,inputs[1])
    txtDeltaT.insert(0,inputs[2])
    txtNumberOfSteps.insert(0,inputs[3])
    txtUFunction.insert(0,inputs[4])
    UpdateLeftStatus("Status: Opened " + filepath)
    UpdateMidStatus("")
    UpdateRightStatus("")
    pltVectorField.clearPlots()
##end OpenSolution()



##
# Method to store a solution to a differential. NOTE: the save process only saves the text from the input fields, after opening a saved solution it is still necessary to click the "Solve IVP" button.
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def SaveSolution(event):
    inputs = [txtDifferential.get(), 
              txtUInitial.get(),
              txtDeltaT.get(), 
              txtNumberOfSteps.get(),
              txtUFunction.get()]
    filepath = tk.filedialog.asksaveasfilename(defaultextension=".ivp", filetypes=(("IVP calculator", "*.ivp"),("All Files", "*.*") ))
    with open(filepath, "w") as toFile:
        for i in inputs:
            toFile.write(i + "\n")
    UpdateLeftStatus("Status: Saved " + filepath)
    UpdateMidStatus("")
    UpdateRightStatus("")
    pltVectorField.clearPlots()
##end SaveSolution



##
# Method to pull up help instructions right inside the Graphical User Interface. The help functions are stored in a text file if there is a preference to simply read them directly.
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def ShowHelp(event):
    dlgHelp = tk.Toplevel(gui)
    dlgHelp.geometry("432x345")
    dlgHelp.title("Initial Value Calculator Help")
    helpString = ""
    with open("resources/ivp_help.txt", "r") as fromFile:
        for line in fromFile:
            helpString = fromFile.read()
    infoHelp = info.InfoDialog(dlgHelp, info=helpString)
    infoHelp.pack(fill="both", expand=True)
##end ShowHelp()


##
# Method to pull up general information about this project directly in the Graphical User Interface. 
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def ShowAbout(event):
    dlgAbout = tk.Toplevel(gui)
    dlgAbout.geometry("432x345")
    dlgAbout.title("About Initial Value Calculator")
    aboutString = ""
    with open("resources/ivp_about.txt", "r") as fromFile:
        for line in fromFile:
            aboutString = fromFile.read()
    infoAbout = info.InfoDialog(dlgAbout, info=aboutString)
    infoAbout.pack(fill="both", expand=True)
##end ShowAbout()


##
# Method to update the "general" portion of the status bar.
# @param leftStatus -string to be displayed on the status bar
def UpdateLeftStatus(leftStatus):
    lblLeftStatus["text"] = leftStatus
##end UpdateStatusLeft()


##
# Method to update the "summary" portion of the status bar, typically will display the time dependent differential equation after solving.
# @param midStatus -string to be displayed on the status bar
def UpdateMidStatus(midStatus):
    lblMidStatus["text"] = midStatus
##end UpdateStatusLeft()


##
# Method to update the "progress" portion of the status bar, typically will display the initial value after solving
# @param rightStatus -string to be displayed on the status bar
def UpdateRightStatus(rightStatus):
    lblRightStatus["text"] = rightStatus
##end UpdateStatusLeft()


def ClearPlots(event):
    pltVectorField.clearPlots()
##end ClearPlots


##
# For test purposes only while developing the plot area vector field
def TestArrow(event):
    # pltVectorField.create_arrow(20, 20, 45, 45)
    # pltVectorField.create_arrow(45, 45, 103, 90)
    # pltVectorField.create_arrow(103, 90, 178, 15)
    # pltVectorField.create_arrow(178, 15, 245, 7)
    
    pltVectorField.setScale([-10, 10], [-100, 100])
    function = "2*x**3 - 8*x**2 + 7" 
    #function = "-x**2"
    x = -10
    previous = [x, eval(function)]
    while x <= 10:
        y = eval(function)
        pltVectorField.create_curve(previous[0], previous[1], x, y)
        previous = [x, y]
        x += 1
        
    x = -11
    previous = [x, eval(function)]
    x = -10
    while x <= 10:
        y = eval(function)
        pltVectorField.create_arrow(previous[0], previous[1], x, y)
        previous = [x, y]
        x += 3
        
##end TestArrow()



##
# Tthe primary function call as per the assignment, it will calculate a two dimensional list containing the solutions found from the time dependent differential using Euler's method as well as calculate a two dimensional list of corresponding exact solutions
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def SolveIVP(event): 
    u = ivp.Exact()
    diff = ivp.EulerMethod()
    if len(txtDeltaT.get()) != 0:
        diff.setDeltaT(txtDeltaT.get())
        u.setDeltaT(txtDeltaT.get())
    if len(txtNumberOfSteps.get()) != 0:
        diff.setSteps(txtNumberOfSteps.get())
        u.setSteps(txtNumberOfSteps.get())
    if len(txtUInitial.get()) != 0:
        diff.setInitialU(txtUInitial.get())
        u.setInitialValue(txtUInitial.get())
    if len(txtUFunction.get()) != 0:
        u.evaluateFunction(txtUFunction.get())
    if len(txtDifferential.get()) != 0:
        ##diff.setSolutionFunctions(txtUFunction.get()) ##I don't think I'm supposed to plug this in for Euler's, that's the improved RK method
        diff.solve(txtDifferential.get())
        diff.minMax()

        ## plot the estimated and exact solutions
    if isinstance(diff.functionU[0], list):
        pltVectorField.setScale(diff.xRange, diff.yRange)
        counter = 1
        previous = [diff.functionU[0][0], diff.functionU[0][1]]
        while counter < len(diff.functionU):
            x = diff.functionU[counter][0]
            y = diff.functionU[counter][1]
            pltVectorField.create_arrow(previous[0], previous[1], x, y)
            previous = [x, y]
            counter += 1
            
        counter = 1
        previous = [u.solutions[0][0], u.solutions[0][1]]
        while counter < len(u.solutions):
            x = u.solutions[0][0]
            y = u.solutions[0][1]
            pltVectorField.create_curve(previous[0], previous[1], x, y)
            previous = [x, y]
            counter += 1
    else:
        ## still need to plot the non-vector differentials
        pass
    

        ## Tables of solutions
    lstIVPSolutions.deltaT = diff.deltaT
    lstIVPSolutions.rows = diff.functionU
    lstIVPSolutions.layout()
    lstExactSolutions.deltaT = u.deltaT
    lstExactSolutions.rows = u.solutions
    lstExactSolutions.layout()
        
    
    # for i in range(0, len(diff.functionU), 2):
    #     pltVectorField.create_arrow(diff.functionU[i][0], diff.functionU[i][1], diff.functionU[i+1][0], diff.functionU[i+1][1])
    
    UpdateLeftStatus("Status: Solved...")
    UpdateMidStatus("F(t, u(t)) = " + str(diff))
    UpdateRightStatus("u(0) = " + str(diff.functionU[0]))
    
##end SolveIVP()





"""
The rest of this script is to put the Graphical User Interface together for Input/Output purposes
"""

######################################  GUI  ##################################

gui = tk.Tk()
gui.geometry("965x532")
gui.title("Initial Value Calculator")




        ############################# MAIN MENU  ###############################
        
mnMain = tk.Menu(gui)

mnFile = tk.Menu(mnMain, tearoff=0)
mnFile.add_command(label="New Solution     ctrl+shift+N", command=lambda: NewSolution(None))
mnFile.add_command(label="Open Solution    crrl+shift+O", command=lambda: OpenSolution(None))
mnFile.add_command(label="Save Solution    ctrl+s", command=lambda: SaveSolution(None))
mnMain.add_cascade(label="File", menu=mnFile)

mnTools = tk.Menu(mnMain, tearoff=0)
mnTools.add_command(label="Solve IVP     ctrl+shift+I", command=lambda: SolveIVP(None))
mnTools.add_command(label="Clear Plots", command=lambda: ClearPlots(None))
mnMain.add_cascade(label="Tools", menu=mnTools)

mnHelp = tk.Menu(mnMain, tearoff=0)
mnHelp.add_command(label="Help", command=lambda: ShowHelp(None))
mnHelp.add_command(label="About", command=lambda: ShowAbout(None))
mnMain.add_cascade(label="Help", menu=mnHelp)


        ###########################  TOOLBAR  ###############################
frmToolbar = tk.Frame(gui, bd=3, relief=tk.RAISED)
btnPlaceholder = tk.Button(frmToolbar, text="test vector", command=lambda: TestArrow(None))
btnSolution = tk.Button(frmToolbar, text="Solve IVP", command=lambda: SolveIVP(None))
btnClearPlot = tk.Button(frmToolbar, text="Clear Plots", command=lambda: ClearPlots(None))


        ###########################  PRIMARY I/O  ############################
ioPrimary = tk.PanedWindow(gui, orient=tk.HORIZONTAL, sashrelief=tk.RAISED)
ioControls = tk.Frame(ioPrimary, bd=3, relief=tk.GROOVE)
ioPlot = tk.Frame(ioPrimary, bd=3, relief=tk.GROOVE)
ioList = tk.Frame(ioPrimary, bd=3, relief=tk.GROOVE)
ioPrimary.add(ioControls)
ioPrimary.add(ioPlot)
ioPrimary.add(ioList)


            ############################  INPUT PANEL  ##############################
            
lblDifferentialInstructions = tk.Label(ioControls, text="Input the Time Dependent Differential Function:\n(in python syntax, use \"u\" and \"v\" for the above functions,\n\"t\" for the variable, and separate piecewise with an \"&\")\nEX: t*math.cos(u**3)*(3*u**2)&(2*t**2)/math.sqrt(t**3)")
lblDifferential = tk.Label(ioControls, text = "u'(t)=F(t, u(t))=")
txtDifferential = tk.Entry(ioControls)


lblInitialInstructions = tk.Label(ioControls, text="Input the inital values:\n(as numbers separated with an ampersand (&))")
lblInitial = tk.Label(ioControls, text="Input the Initial Values:")
lblUInitial = tk.Label(ioControls, text="u(0)=")
txtUInitial = tk.Entry(ioControls)


lblDeltaTInstructions = tk.Label(ioControls, text="Input the Time Interval and Number of steps to take:\n(as a number)")
lblDeltaT = tk.Label(ioControls, text="\u0394t=")
txtDeltaT = tk.Entry(ioControls)
lblNumberOfSteps = tk.Label(ioControls, text="Steps=")
txtNumberOfSteps = tk.Entry(ioControls)


lblFunctionInstructions = tk.Label(ioControls, text="Input the Exact Solution Functions:\n(in Python syntax using t as the variable, or a comma separated list for a set)\nEX: 3*math.sqrt(2*t - t // 3) & 2*math.sin(3*t**2) OR 4, 7, 18, 31, ...")
lblUFunction = tk.Label(ioControls, text="u(t)=")
txtUFunction = tk.Entry(ioControls)



        ##############################  PLOTTING PANEL  #################################
        
squareSize = 300
pltVectorField = vf.VectorField(ioPlot, width=squareSize, height=squareSize)



        #############################  EVALUTATION TABLE  ###############################

#lstSolutions = tk.Listbox(ioList)
lstIVPSolutions = table.Table(ioList, rows=[[0, 0]], title="IVP Solution")
lstExactSolutions = table.Table(ioList, [[1, 1]], title="Exact Solution")



        ###########################  STATUS BAR  ############################
frmStatus = tk.Frame(gui, bd=3, relief=tk.SUNKEN)
lblLeftStatus = tk.Label(frmStatus, text="Status: Ready to begin ...")
lblMidStatus = tk.Label(frmStatus, text="<summary>")
lblRightStatus = tk.Label(frmStatus, text="<results>")


        ############################  LOAD CONTROLS  #########################
    ## main containers
gui.config(menu=mnMain)
frmToolbar.pack(fill="both")
ioPrimary.pack(fill="both", expand=True)
frmStatus.pack(fill="both")


    ## toolbar
btnPlaceholder.grid(row=0, column=0, padx=5, pady=10)
btnSolution.grid(row=0, column=1, padx=5, pady=10)
btnClearPlot.grid(row=0, column=2, padx=5, pady=10)

    ## input fields
lblDifferentialInstructions.grid(row=0, column=0, columnspan=4, pady=7)
lblDifferential.grid(row=1, column=0)
txtDifferential.grid(row=1, column=1, columnspan=3, sticky="EW")


lblInitialInstructions.grid(row=2, column=0, columnspan=4, pady=7)
lblUInitial.grid(row=3, column=0)
txtUInitial.grid(row=3, column=1, columnspan=3, sticky="EW")


lblDeltaTInstructions.grid(row=4, column=0, columnspan=4, pady=7)
lblDeltaT.grid(row=5, column=0)
txtDeltaT.grid(row=5, column=1)
lblNumberOfSteps.grid(row=5, column=2)
txtNumberOfSteps.grid(row=5, column=3)

lblFunctionInstructions.grid(row=6, column=0, columnspan=4, pady=7)
lblUFunction.grid(row=7, column=0)
txtUFunction.grid(row=7, column=1, columnspan=3, sticky="EW")

    ## plot area
pltVectorField.grid(row=0, column=1, padx=10, pady=10)

    ## solutions table
lstIVPSolutions.pack(fill="both", expand=True)
lstExactSolutions.pack(fill="both", expand=True)


    ## status bar

lblLeftStatus.pack(side="left")

lblRightStatus.pack(side="right")
lblMidStatus.pack(side="right", padx=20)



        ############################  KEYBOARD SHORTCUTS  ####################
gui.bind("<Control-Shift-KeyPress-N>", lambda event: NewSolution(event))
gui.bind("<Control-Shift-KeyPress-O>", lambda event: OpenSolution(event))
gui.bind("<Control-KeyPress-s>", lambda event: SaveSolution(event))
gui.bind("<Control-Shift-KeyPress-I>", lambda event: SolveIVP(event))



if __name__=="__main__":
    NewSolution(None)
    gui.mainloop()
    
















#####################  WHITE SPACE FOR SCROLLING  #########################