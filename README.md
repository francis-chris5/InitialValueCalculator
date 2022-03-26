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

<p>Here's a picture of the progress so far... I don't know why the y component on the vectors is blowing up right now... NOTE: the arrows and function on the vector field are test cases only and are completely unrelated to the IVP (test was: 2*x**3 - 8*x**2 + 7)</p>

<img src="https://user-images.githubusercontent.com/50467171/160255630-b5901f19-7970-4de9-b075-18dd932bd96c.png"/>

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

