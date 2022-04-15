# InitialValueCalculator

<h2>Project Synopsis</h2>
<p>The application designed to estimate the solutions for time dependent differential equations using Euler’s Method was developed using the Python programming language with no libraries external to the default version of the language. Default libraries means that the Input/Output is handled in a tkinter Graphical User Interface (GUI), and by far the majority of the code written is for the GUI and not directly solving the time dependent differential equation for a given initial value.</p>
<p>Differentials of one or two dimensions (in excess of time) can be input along with a time interval to apply the estimation method and a number of steps to take. When available an exact solution to the differential can also be input for comparative purposes. The results are displayed graphically and in table format, with the option to export the tables to a CSV file for compatibility with other software.</p>
<p>The package containing all relevant files includes a version of a Lorenz Attractor and a random example from an undergrad differential equations textbook for proof of concept samples.</p>


<h3>Input Fields</h3>
<p>On the left hand side of the GUI are input fields for the (1)time dependent differential, (2)the initial values, (3)the step size to take, and the (4)number of steps to take, along with an optional field to input the (5)exact solution to the differential.</p>

<img src="https://user-images.githubusercontent.com/50467171/163650178-01afd995-7139-4f9a-a1f5-295df9b1bfad.png"/>


<ol>
  <li>If the differential is composed of a function in a single dimension, with time as the only independent variable the function is input directly in python notation. Python’s “math” module is available for use when necessary, e.g. math.sqrt(x) or math.cos(x). If the differential is made up of multiple functions, vector input, then separate the functions with an ampersand (&).</li>
<li>The initial values need to be numeric input, if more than one dimension is needed separate the numbers using an ampersand (&).</li>
<li>The time interval size to be used in solving the differential with Euler’s Method needs entered directly.</li>
<li>An integer number to request a specific number of iterations to run through Euler’s Method for estimating the solution to a differential equation.</li>
<li>(Optional) When an exact solution is known the function(s) can be entered into this input field to be plotted alongside the estimate from using Euler’s Method for a visual comparison of the results.</li>

</ol>


<h3>Outputs</h3>
<p>The middle and right-hand side of the GUI contains output areas. (1) The iterated estimates from using Euler’s Method are plotted in black arrows, and the exact solution is plotted with a red line –the red line is narrower and will appear above the black arrows–, (2) a table listing out the time and value for each dimension at that time from the Euler’s Method estimate is found at the top left, with (3) a table listing out the exact solution for the same time intervals below it when the exact solutions are known, along with an option to (4) export the tables for the estimated and exact values to a CSV file for use with other software when needed.</p>


<img src="https://user-images.githubusercontent.com/50467171/163650184-e5dd39e4-8ce2-4352-b73d-2f566eab5244.png"


<h3>Software</h3>
<p>The scripts composing this piece of software were created using only the default installation of Python 3.10.2 and are organized into a package as follows. At the top level is the script called ivp_app.py which is the main script along with two example files: the two dimensional Lorenz solution (shown in the screenshots above) and a randomly selected one dimensional example from an undergrad textbook on differential equations in the Euler’s Method section. The main script (ivp_app.py) is lengthy and almost entirely related to the GUI, the relevant methods to the requested problem are found between lines [175 and 285] where the methods to plot and to calculate the solutions are found. </p>
<p>The second level in the hierarchy contains folders called images, lib, and resources. The resources folder contains text files holding data for the “Help” and “About” functions in the software. The images folder contains the icons for the toolbar buttons. The lib folder contains the custom classes for this project.</p>
<p>	The files infodialog.py, scrollframe.py, and table.py all relate to formatting items on the GUI. The other two scripts ivp.py and vectorfield.py relate to the assigned project. The ivp.py script contains two classes Exact and EulerMethod. </p>
<p>The Exact class is for processing the exact solutions to the differential for comparison to the estimates when the solution is known and entered into the appropriate input field on the GUI. Exact solutions can be entered as a single function, a vector of functions with each dimension delimited by an ampersand (&), or as a comma separated list of values for discrete sets. The Exact class will split things up into lists and evaluate functions as necessary to get the solutions ready for the tabular and plotting output areas for comparison to the estimated solutions using Euler’s Method.</p>
<p>The EulerMethod class will take the time dependent differential input to the corresponding field on the GUI as either a one or two dimensional vector of functions, using an ampersand (&) to delimit multiple dimensions of the vector. It then uses Euler’s Method to estimate the solution at each given time interval and creates a multi-dimensional list of solutions for the tabular and plotted output areas, including the values to select an appropriate scale for the plot.</p>
<p>In the vectorfield.py script is a custom subclass of the tkinter.canvas widget to be used for a plot area. The class draws a horizontal and vertical axis, and includes methods to set the scale values for both the x and y axis, plotting a thin red curve (for exact solutions), and plotting a thick black arrow (for estimated solutions).</p>
<p>Comments were entered in Doxygen format, and the website generated for code documentation is in a directory parallel to the InitialValueCalculator_tkinter directory. The entire project can also be found in the repository located at https://github.com/francis-chris5/InitialValueCalculator .</p>
<p>Each “solution” input to the software (New → Save → Open) contains an instance of the EulerMethod and Exact classes. Functions in the primarily GUI script of ivp_app.py on  lines [enter numbers] call the appropriate methods from these classes to load data from the inputs, process the solutions, and output the results. Once the results have been output an option will become available to export the tabular results to CSV files for compatibility with other software to make further use of these solutions.</p>


<h3>Development Process</h3>
<p>	In general the development process went smoothly. Upon first hearing the assignment instructions I had a great many ideas run through my head, many of which could not be confined to within the available time constraints (though a number of comments for where these ideas should be positioned in the code were placed along the way). A traditional appearance for a Graphical User Interface (GUI) to input the differential and values needed to estimate a solution, along with a way to input an exact solution was the initial focus, along with a way to display the numerical and graphical results (without the use of external libraries). Some traditional options for software, new - open - save,  seemed appropriate as these input values would likely not be easy to input so that only having to do so once would surely be a benefit. Since Python is an interpreted language a programmer has direct access to the same method the Python Interpreter calls to run each line of text based code without the need for a compiler, so I decided to use this allowing the functions to be input with regular python syntax. This decision required Python’s “math” library to be included with the objects carrying the bulk of the processing load since time dependent differentials will most likely include functions that would lead to chain rule derivatives such as roots, exponentials, and trigonometric functions. Most of the work went towards the GUI as the plan came together without any big issues, most of the debugging revolved around typos. There were more features I would have like to added but time ran short and a couple ideas for expansion that would be useful: most notably, the inclusion of the mathplotlib library which is not part of the Python language would allow much better plotting (I ran out of time to get even a basic zoom feature included) as well as what’s commonly known as “LaTex” input/output –even though the input isn’t actually latex, it’s the input used on some commonly known and heavily used pieces of software such as Pearson’s MyMathLab or the Desmos online graphing calculator, far better input options for something like this than the Python language alone allows for without extensive customization of the inputs classes. In summary the project went very well and this may even be a piece of software I hope to expand on in the future.</p>

