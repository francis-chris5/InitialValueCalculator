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


testIVP = ivp.IVP(time=0, function="sqrt(x^3)")

#######################################  Functions  ##########################

def NewSolution(event):
    print("new solution coming soon")
##end NewSolution()


def OpenSolution(event):
    print("open solution coming soon")
##end OpenSolution()


def SaveSolution(event):
    print("save solution coming soon")
##end SaveSolution


def PrintSolution(event):
    filepath = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("text file", "*.txt"),("All Files", "*.*") ))
    with open(filepath, "w") as toFile:
        toFile.write(str(testIVP))
##end PrintSolution()


def ShowHelp(event):
    dlgHelp = tk.Toplevel(gui)
    dlgHelp.geometry("432x345")
    dlgHelp.title("Initial Value Calculator Help")
    helpString = ""
    with open("resources/ivp_help.txt", "r") as fromFile:
        for line in fromFile:
            helpString = fromFile.read()
    lblHelp = tk.Label(dlgHelp, text=helpString, wraplength=400, justify=tk.LEFT)
    lblHelp.pack(side="left", padx=10, pady=10)
##end ShowHelp()


def ShowAbout(event):
    dlgAbout = tk.Toplevel(gui)
    dlgAbout.geometry("432x345")
    dlgAbout.title("About Initial Value Calculator")
    aboutString = ""
    with open("resources/ivp_about.txt", "r") as fromFile:
        for line in fromFile:
            aboutString = fromFile.read()
    lblAbout = tk.Label(dlgAbout, text=aboutString, wraplength=400, justify=tk.LEFT)
    lblAbout.pack(side="left", padx=10, pady=10)
##end ShowAbout()






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
btnPlaceholder = tk.Button(frmToolbar, text="placeholder")


        ###########################  PRIMARY I/O  ############################
ioPrimary = tk.PanedWindow(gui, orient=tk.HORIZONTAL, sashrelief=tk.RAISED)
ioControls = tk.Frame(ioPrimary, bd=3, relief=tk.GROOVE)
ioPlot = tk.Frame(ioPrimary, bd=3, relief=tk.GROOVE)
ioPrimary.add(ioControls)
ioPrimary.add(ioPlot)

lblStuff = tk.Label(ioControls, text="control widgets")
pltVectorField = vf.VectorField(ioPlot, deltaX = 0.1)
#pltVectorField.create_arrow(20, 20, 45, 45)
pltVectorField.plot(a=1, b=4)



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
lblStuff.grid(row=0, column=0, padx=10, pady=20)
#lblFiller.grid(row=0, column=0, padx=10, pady=20)
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