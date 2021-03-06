"""
NOTE: the lines that relate to the project are lines [161 - 226]** CHANGE THIS AT SUBMISSION: SolveIVP method, the bulk of the problem at hand is in the file ivp.py located in the lib folder.
"""

##
# @mainpage <h1>Initial Value Calculator</h1><h3>1.0.1</h3> 
# <p>The application designed to estimate the solutions for time dependent differential equations using Euler’s Method was developed using the Python programming language with no libraries external to the default version of the language. Default libraries means that the Input/Output is handled in a tkinter Graphical User Interface (GUI), and by far the majority of the code written is for the GUI and not directly solving the time dependent differential equation for a given initial value.</p> <p>Differentials of one or two dimensions (in excess of time) can be input along with a time interval to apply the estimation method and a number of steps to take. When available an exact solution to the differential can also be input for comparative purposes. The results are displayed graphically and in table format, with the option to export the tables to a CSV file for compatibility with other software.</p>
# @author Christopher S. Francis

## Part of python language
import tkinter as tk
import tkinter.filedialog as fd
import csv

## custom libraries for this project
import lib.ivp as ivp
import lib.vectorfield as vf
import lib.infodialog as info
import lib.table as table
import lib.scrollframe as scroll


u = ivp.Exact()
diff = ivp.EulerMethod()

#######################################  Functions  ##########################

##
# Method to reset the GUI for a new solution to be entered.
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def NewSolution(event):
    global diff, u
    u = ivp.Exact()
    diff = ivp.EulerMethod()
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
    pltVectorField.xScale = 1
    pltVectorField.yScale = 1
    btnToCSV["state"] = "disabled"
##end NewSolution()


##
# Method to retrieve a previously solved solution. The application files include a version of the Lorenz Attractor to demonstrate how to input differentials and exact solutions. NOTE: the save process only saves the text from the input fields, after opening a saved solution it is still necessary to click the "Solve IVP" button.
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def OpenSolution(event):
    ##should probably put a want to save dialog here
    global diff, u
    u = ivp.Exact()
    diff = ivp.EulerMethod()
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
    pltVectorField.xScale = 1
    pltVectorField.yScale = 1
    btnToCSV["state"] = "disabled"
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

def ShowError(event, errorString):
    dlgError = tk.Toplevel(gui)
    dlgError.geometry("432x345")
    dlgError.title("About Initial Value Calculator")
    aboutString = ""
    infoError = info.InfoDialog(dlgError, info=errorString)
    infoError.pack(fill="both", expand=True)
##end ShowError()


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









# =============================================================================
#  THIS PART RELATES DIRECTLY TO THE ASSIGNMENT
# =============================================================================


def ClearPlots(event):
    pltVectorField.clearPlots()
##end ClearPlots


def PlotSolution(event):
        ## plot the estimated and exact solutions
    if isinstance(diff.functionU[0], list):
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
            x = u.solutions[counter][0]
            y = u.solutions[counter][1]
            pltVectorField.create_curve(previous[0], previous[1], x, y)
            previous = [x, y]
            counter += 1
    elif not isinstance(diff.functionU[0], list):
        pltVectorField.setScale(diff.xRange, diff.yRange)
        estimate = []
        for i, x in enumerate(diff.functionU):
            estimate.append([diff.deltaT * i, x])
        counter = 1
        previous = [estimate[0][0], estimate[0][1]]
        while counter < len(diff.functionU):
            x = estimate[counter][0]
            y = estimate[counter][1]
            pltVectorField.create_arrow(previous[0], previous[1], x, y)
            previous = [x, y]
            counter += 1
        
        if len(u.solutions) > 1:
            actual = []
            for i, x in enumerate(u.solutions):
                actual.append([u.deltaT * i, x])
            counter = 1
            previous = [actual[0][0], actual[0][1]]
            while counter < len(u.solutions):
                x = actual[counter][0]
                y = actual[counter][1]
                pltVectorField.create_curve(previous[0], previous[1], x, y)
                previous = [x, y]
                counter += 1
##end PlotSolution()


def ZoomIn(event):
    ## uhm... nothing seems to work right with zoom, in out do the same thing for +- and */
    #if pltVectorField.xScale > 100 and pltVectorField.yScale > 100:
    pltVectorField.xScale /= 1.5
    pltVectorField.yScale /= 1.5
    ClearPlots(None)
    PlotSolution(None)
##end ZoomIn()


def ZoomOut(event):
    pltVectorField.xScale *= 1.5
    pltVectorField.yScale *= 1.5
    ClearPlots(None)
    PlotSolution(None)
##end ZoomOut()





##
# Tthe primary function call as per the assignment, it will calculate a two dimensional list containing the solutions found from the time dependent differential using Euler's method as well as calculate a two dimensional list of corresponding exact solutions
# @param event -the hardware event used to call this method --probably not used in a simple application such as this.
def SolveIVP(event): 
    # u = ivp.Exact()
    # diff = ivp.EulerMethod()
    if len(txtDeltaT.get()) != 0:
        diff.setDeltaT(txtDeltaT.get())
        u.setDeltaT(txtDeltaT.get())
    else:
        diff.setDeltaT("0.1")
        u.setDeltaT("0.1")
        
    if len(txtNumberOfSteps.get()) != 0:
        diff.setSteps(txtNumberOfSteps.get())
        u.setSteps(txtNumberOfSteps.get())
    else:
        diff.setSteps("5")
        u.setSteps("5")
        
    if len(txtUInitial.get()) != 0:
        diff.setInitialU(txtUInitial.get())
        u.setInitialValue(txtUInitial.get())
    else:
        diff.setInitialU("0")
        u.setInitialValue("0")
        
    if len(txtUFunction.get()) != 0:
        u.evaluateFunction(txtUFunction.get())
    else:
        ## the exact solution is optional
        pass
        
    if len(txtDifferential.get()) != 0:
        ##diff.setSolutionFunctions(txtUFunction.get()) ##I don't think I'm supposed to plug this in for Euler's, that's the improved RK method
        diff.solve(txtDifferential.get())
        diff.minMax()
    else:
        diff.solve("u + t") ## defaults to a linear solution
        ShowError(None, "A time dependent differential must be entered, to prevent a total crash the software will work with the function f(t, u(t)) = u")
        
    pltVectorField.setScale(diff.xRange, diff.yRange)
    PlotSolution(None)
        
        ## Tables of solutions
    lstIVPSolutions.deltaT = diff.deltaT
    lstIVPSolutions.rows = diff.functionU
    lstIVPSolutions.layout()
    lstExactSolutions.deltaT = u.deltaT
    lstExactSolutions.rows = u.solutions
    lstExactSolutions.layout()


    UpdateLeftStatus("Status: Solved...")
    UpdateMidStatus("F(t, u(t)) = " + str(diff))
    UpdateRightStatus("u(0) = " + str(diff.functionU[0]))
    
    btnToCSV["state"] = "normal"
    
##end SolveIVP()





# =============================================================================
#  THE STUFF ABOVE THIS PART RELATES DIRECTLY TO THE ASSIGNMENT
# =============================================================================









def ExportCSV(event):
    filepath = fd.asksaveasfilename()
    estimate = filepath + "_euler_method.csv"
    exact = filepath + "_exact.csv"
    with open(estimate, "w") as toFile:
        writer = csv.writer(toFile)
        for vector in diff.functionU:
            if isinstance(vector, float):
                vector = [vector]
            writer.writerow(vector)
    with open(exact, "w") as toFile:
        writer = csv.writer(toFile)
        for vector in u.solutions:
            if isinstance(vector, float):
                vector = [vector]
            writer.writerow(vector)
##end ExportCSV()





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
mnTools.add_command(label="Clear Plots   ctrl+shift+L", command=lambda: ClearPlots(None))
mnMain.add_cascade(label="Tools", menu=mnTools)

mnHelp = tk.Menu(mnMain, tearoff=0)
mnHelp.add_command(label="Help", command=lambda: ShowHelp(None))
mnHelp.add_command(label="About", command=lambda: ShowAbout(None))
mnMain.add_cascade(label="Help", menu=mnHelp)


        ###########################  TOOLBAR  ###############################
frmToolbar = tk.Frame(gui, bd=3, relief=tk.RAISED)
imgNew = tk.PhotoImage(file="images/new.png")
imgOpen = tk.PhotoImage(file="images/open.png")
imgSave = tk.PhotoImage(file="images/save.png")
imgSolve = tk.PhotoImage(file="images/solve.png")
imgClear = tk.PhotoImage(file="images/clear.png")
imgHelp = tk.PhotoImage(file="images/help.png")
btnNew = tk.Button(frmToolbar, image=imgNew, command=lambda: NewSolution(None))
btnOpen = tk.Button(frmToolbar, image=imgOpen, command=lambda: OpenSolution(None))
btnSave = tk.Button(frmToolbar, image=imgSave, command=lambda: SaveSolution(None))
btnSolution = tk.Button(frmToolbar, image=imgSolve, command=lambda: SolveIVP(None))
btnClearPlot = tk.Button(frmToolbar, image=imgClear, command=lambda: ClearPlots(None))
btnHelp = tk.Button(frmToolbar, image=imgHelp, command=lambda: ShowHelp(None))



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
pltVectorField = vf.VectorField(ioPlot, width=squareSize, height=squareSize, border=2, relief="groove")
btnZoomIn = tk.Button(ioPlot, text="Zoom In", command=lambda: ZoomIn(None))
btnZoomOut = tk.Button(ioPlot, text="Zoom Out", command=lambda: ZoomOut(None))


        #############################  EVALUTATION TABLE  ###############################

#lstSolutions = tk.Listbox(ioList)
btnToCSV = tk.Button(ioList, text="Export to CSV file", command=lambda: ExportCSV(None), state="disabled")
frmUpper = tk.Frame(ioList)
frmLower = tk.Frame(ioList)
scrSolutionList = scroll.ScrollFrame(frmUpper)
scrExactList = scroll.ScrollFrame(frmLower)
lstIVPSolutions = table.Table(scrSolutionList.frmContent, rows=[[0, 0]], title="IVP Solution")
lstExactSolutions = table.Table(scrExactList.frmContent, rows=[[1, 1]], title="Exact Solution")



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
btnNew.grid(row=0, column=0, padx=5, pady=10)
btnOpen.grid(row=0, column=1, padx=5, pady=10)
btnSave.grid(row=0, column=2, padx=5, pady=10)
btnSolution.grid(row=0, column=3, padx=5, pady=10)
btnClearPlot.grid(row=0, column=4, padx=5, pady=10)
btnHelp.grid(row=0, column=5, padx=5, pady=10)

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
pltVectorField.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
#btnZoomIn.grid(row=1, column=0, padx=10, pady=25)
#btnZoomOut.grid(row=1, column=1, padx=10, pady=25)

    ## solutions table
btnToCSV.pack(fill="both")
frmUpper.pack(fill="both", expand=True)
frmLower.pack(fill="both", expand=True)
scrSolutionList.pack(fill="both", expand=True)
lstIVPSolutions.pack(fill="both", expand=True)
scrExactList.pack(fill="both", expand=True)
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
gui.bind("<Control-Shift-KeyPress-L>", lambda event: ClearPlots(event))



if __name__=="__main__":
    NewSolution(None)
    gui.mainloop()
    
















#####################  WHITE SPACE FOR SCROLLING  #########################