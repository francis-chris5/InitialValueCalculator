# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:36:14 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import tkinter as tk
import tkinter.filedialog
import lib.ivp as ivp
import lib.vectorfield as vf


u = ivp.Exact()
v = ivp.Exact()
diff = ivp.EulerMethod()

#######################################  Functions  ##########################

def NewSolution(event):
    print("new solution coming soon")
##end NewSolution()


def OpenSolution(event):
    inputs = []
    filepath = tk.filedialog.askopenfilename(defaultextension=".ivp", filetypes=(("IVP calculator", "*.ivp"),("All Files", "*.*") ))
    with open(filepath, "r") as fromFile:
        for line in fromFile:
            inputs.append(line.strip())
    txtUFunction.delete(0, tk.END)
    txtVFunction.delete(0, tk.END)
    txtUInitial.delete(0, tk.END)
    txtVInitial.delete(0, tk.END)
    txtDeltaT.delete(0, tk.END)
    txtTargetT.delete(0, tk.END)
    txtDifferential.delete(0, tk.END)
    txtUFunction.insert(0,inputs[0])
    txtVFunction.insert(0,inputs[1])
    txtUInitial.insert(0,inputs[2])
    txtVInitial.insert(0,inputs[3])
    txtDeltaT.insert(0,inputs[4])
    txtTargetT.insert(0,inputs[5])
    txtDifferential.insert(0,inputs[6])
##end OpenSolution()


def SaveSolution(event):
    inputs = [txtUFunction.get(), 
              txtVFunction.get(), 
              txtUInitial.get(),
              txtVInitial.get(),
              txtDeltaT.get(), 
              txtTargetT.get(), 
              txtDifferential.get()
              ]
    filepath = tk.filedialog.asksaveasfilename(defaultextension=".ivp", filetypes=(("IVP calculator", "*.ivp"),("All Files", "*.*") ))
    with open(filepath, "w") as toFile:
        for i in inputs:
            toFile.write(i + "\n")
##end SaveSolution


def PrintSolution(event):
    filepath = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("text file", "*.txt"),("All Files", "*.*") ))
    with open(filepath, "w") as toFile:
        toFile.write(str(u))
##end PrintSolution()


def ShowHelp(event):
    dlgHelp = tk.Toplevel(gui)
    #dlgHelp.geometry("432x345")
    dlgHelp.title("Initial Value Calculator Help")
    helpString = ""
    with open("resources/ivp_help.txt", "r") as fromFile:
        for line in fromFile:
            helpString = fromFile.read()
    lblHelp = tk.Label(dlgHelp, text=helpString, wraplength=500, justify=tk.LEFT)
    lblHelp.pack(side="left", padx=10, pady=10)
##end ShowHelp()


def ShowAbout(event):
    dlgAbout = tk.Toplevel(gui)
    #dlgAbout.geometry("432x345")
    dlgAbout.title("About Initial Value Calculator")
    aboutString = ""
    with open("resources/ivp_about.txt", "r") as fromFile:
        for line in fromFile:
            aboutString = fromFile.read()
    lblAbout = tk.Label(dlgAbout, text=aboutString, wraplength=400, justify=tk.LEFT)
    lblAbout.pack(side="left", padx=10, pady=10)
##end ShowAbout()



def TestArrow(event):
    pltVectorField.create_arrow(20, 20, 45, 45)
    pltVectorField.create_arrow(45, 45, 103, 90)
    pltVectorField.create_arrow(103, 90, 178, 15)
    pltVectorField.create_arrow(178, 15, 245, 7)
##end TestArrow()


def TestFunction(event):
    if len(txtDeltaT.get()) != 0:
        diff.setDeltaT(txtDeltaT.get())
        u.setDeltaT(txtDeltaT.get())
        v.setDeltaT(txtDeltaT.get())
    if len(txtTargetT.get()) != 0:
        diff.setTargetT(txtTargetT.get())
        u.setTargetT(txtTargetT.get())
        v.setTargetT(txtTargetT.get())
    if len(txtUInitial.get()) != 0:
        diff.setInitialU(txtUInitial.get())
        u.setInitialValue(txtUInitial.get())
    if len(txtVInitial.get()) != 0:
        diff.setInitialV(txtVInitial.get())
        v.setInitialValue(txtVInitial.get())
    if len(txtUFunction.get()) != 0:
        u.evaluateFunction(txtUFunction.get())
    if len(txtVFunction.get()) != 0:
        v.evaluateFunction(txtVFunction.get())
    if len(txtDifferential.get()) != 0:
        diff.solve(txtDifferential.get())
    
##end TestFunction()




######################################  GUI  ##################################

gui = tk.Tk()
gui.geometry("765x432")
gui.title("Initial Value Calculator")



## menu -new, open, save, print -help, about



"""
menu and tool bar: file tools help
main content: left panel sliders and input boxes, right side plot of the solution
status bar: left display the differential, middle ??, right ??
"""
        ############################# MAIN MENU  ###############################
        
mnMain = tk.Menu(gui)

mnFile = tk.Menu(mnMain, tearoff=0)
mnFile.add_command(label="New Solution     ctrl+shift+N", command=lambda: NewSolution(None))
mnFile.add_command(label="Open Solution", command=lambda: OpenSolution(None))
mnFile.add_command(label="Save Solution", command=lambda: SaveSolution(None))
mnFile.add_separator()
mnFile.add_command(label="Print Solution", command=lambda: PrintSolution(None))
mnMain.add_cascade(label="File", menu=mnFile)

mnTools = tk.Menu(mnMain, tearoff=0)
mnMain.add_cascade(label="Tools", menu=mnTools)

mnHelp = tk.Menu(mnMain, tearoff=0)
mnHelp.add_command(label="Help", command=lambda: ShowHelp(None))
mnHelp.add_command(label="About", command=lambda: ShowAbout(None))
mnMain.add_cascade(label="Help", menu=mnHelp)


        ###########################  TOOLBAR  ###############################
frmToolbar = tk.Frame(gui, bd=3, relief=tk.RAISED)
btnPlaceholder = tk.Button(frmToolbar, text="test vector", command=lambda: TestArrow(None))
btnTemporary = tk.Button(frmToolbar, text="test inputs", command=lambda: TestFunction(None))


        ###########################  PRIMARY I/O  ############################
ioPrimary = tk.PanedWindow(gui, orient=tk.HORIZONTAL, sashrelief=tk.RAISED)
ioControls = tk.Frame(ioPrimary, bd=3, relief=tk.GROOVE)
ioPlot = tk.Frame(ioPrimary, bd=3, relief=tk.GROOVE)
ioPrimary.add(ioControls)
ioPrimary.add(ioPlot)

lblFunctionInstructions = tk.Label(ioControls, text="Input the Time Dependent Function:\n(in Python syntax using t as the variable, or a comma separated list for a set)\nEX: 3*math.sqrt(2*t - t // 3) OR 4, 7, 18, 31, ...")
lblUFunction = tk.Label(ioControls, text="u(t)=")
txtUFunction = tk.Entry(ioControls)
txtVFunction = tk.Entry(ioControls)
lblVFunction = tk.Label(ioControls, text="v(t)=")


lblInitialInstructions = tk.Label(ioControls, text="Input the inital values:\n(as a number)")
lblInitial = tk.Label(ioControls, text="Input the Initial Values:")
lblUInitial = tk.Label(ioControls, text="u(0)=")
lblVInitial = tk.Label(ioControls, text="v(0)=")
txtUInitial = tk.Entry(ioControls)
txtVInitial = tk.Entry(ioControls)


lblDeltaTInstructions = tk.Label(ioControls, text="Input the Time Interval and Target Time:\n(as a number)")
lblDeltaT = tk.Label(ioControls, text="\u0394t=")
txtDeltaT = tk.Entry(ioControls)
lblTargetT = tk.Label(ioControls, text="target=")
txtTargetT = tk.Entry(ioControls)

lblDifferentialInstructions = tk.Label(ioControls, text="Input the Time Dependent Differential Function:\n(in python syntax, use \"u\" and \"v\" for the above functions,\nseparate piecewise with an \"&\")\nEX: t*math.cos(u**3)*(3*u**2)&(2*t**2)/math.sqrt(t**3)")
lblDifferential = tk.Label(ioControls, text = "u'(t)=F(t, u(t))=")
txtDifferential = tk.Entry(ioControls)


squareSize = 300
pltVectorField = vf.VectorField(ioPlot, width=squareSize, height=squareSize, deltaX = 0.1)
#pltVectorField.create_arrow(20, 20, 45, 45)
#pltVectorField.plot(a=1, b=4)



        ###########################  STATUS BAR  ############################
frmStatus = tk.Frame(gui, bd=3, relief=tk.SUNKEN)
lblLeftStatus = tk.Label(frmStatus, text="Status: ...")
lblMidStatus = tk.Label(frmStatus, text="<progress>")
lblRightStatus = tk.Label(frmStatus, text="<summary>")


        ############################  LOAD CONTROLS  #########################
gui.config(menu=mnMain)
frmToolbar.pack(fill="both")
ioPrimary.pack(fill="both", expand=True)
frmStatus.pack(fill="both")


btnPlaceholder.grid(row=0, column=0, padx=5, pady=10)
btnTemporary.grid(row=0, column=1, padx=5, pady=10)

lblFunctionInstructions.grid(row=0, column=0, columnspan=4, pady=7)
lblUFunction.grid(row=1, column=0)
txtUFunction.grid(row=1, column=1)
lblVFunction.grid(row=1, column=2)
txtVFunction.grid(row=1, column=3)

lblInitialInstructions.grid(row=2, column=0, columnspan=4, pady=7)
lblUInitial.grid(row=3, column=0)
txtUInitial.grid(row=3, column=1)
lblVInitial.grid(row=3, column=2)
txtVInitial.grid(row=3, column=3)

lblDeltaTInstructions.grid(row=4, column=0, columnspan=4, pady=7)
lblDeltaT.grid(row=5, column=0)
txtDeltaT.grid(row=5, column=1)
lblTargetT.grid(row=5, column=2)
txtTargetT.grid(row=5, column=3)

lblDifferentialInstructions.grid(row=6, column=0, columnspan=4, pady=7)
lblDifferential.grid(row=7, column=0)
txtDifferential.grid(row=7, column=1, columnspan=3, sticky="EW")

pltVectorField.grid(row=0, column=1, padx=10, pady=10)

lblLeftStatus.grid(row=0, column=0, padx=90)
lblMidStatus.grid(row=0, column=1, padx=90)
lblRightStatus.grid(row=0, column=2, padx=90)



        ############################  KEYBOARD SHORTCUTS  ####################
gui.bind("<Control-Shift-KeyPress-N>", lambda event: NewSolution(event))
gui.bind("<Control-Shift-KeyPress-O>", lambda event: OpenSolution(event))
gui.bind("<Control-KeyPress-s>", lambda event: SaveSolution(event))
gui.bind("<Control-Shift-KeyPress-P>", lambda event: PrintSolution(event))

gui.mainloop()

















#####################  WHITE SPACE FOR SCROLLING  #########################