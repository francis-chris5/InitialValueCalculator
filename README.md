# InitialValueCalculator
A project in a Mathematical Modeling class, number MATH 537 at Indiana State University, was to write a program that solves time dependent ODE's as Initial Value Problems using Euler's Method.


<h2>Progress</h2>
<ul>
  <li>got the GUI coming together nicely</li>
  <li>working on help menu and about along the way</li>
  <li>reads in IVP differential for 1 or 2 dimensional vector (delimited with an ampersand) with initial values, delta t, and number of steps</li>
  <li>reads in exact solution to IVP in 2d or 3d, or as a discrete set and finds exact value for each time step for comparison --need to plot lines for this</li>
  <li>saves and opens problems</li>
  <li>displays the numerical results in a "table" --this needs a lot of formatting work, maybe even a different widget on the GUI</li>
  <li>plotter displays vector based off the input global coordinates --need to set up scale based off solutions</li>
</ul>

<p>Here's a picture of the progress so far... I don't know why the y component on the vectors is blowing up right nowNOTE: the arrows on the vector field are test arrows only and are completely unrelated to the function that was input</p>

<img src="https://user-images.githubusercontent.com/50467171/160249969-10e57822-3e3a-4a92-971e-f2920cf61136.png"/>

<br>
<br>
<br>
<h2>Remaining To-Do</h2>
<ul>
  <li>BUG: for some reasons the y component of the vector is increasing too rapidly on each step (in pic above should be 1.450 instead of 2.450) that carries through each step</li>
  <li>lots of other stuff</li>
  <li>polish up the final project</li>
  <li>add code that has no purpose, i.e. comments</li>
</ul>
<br>
<br>

