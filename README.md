# InitialValueCalculator
A project in a Mathematical Modeling class, number MATH 537 at Indiana State University, was to write a program that solves time dependent ODE's as Initial Value Problems using Euler's Method.


<h3>Phase 1 Complete</h3>
<ul>
  <li>Got the rough plan for the interface together</li>
  <li>User manual being built while each step is being debugged, available under help menu</li>
  <li>It can process the functions when they're given as a string, both continuous and discrete sets</li>
  <li>works with or without a user given delta time (0.1 is the default)</li>
  <li>arrows can be drawn on the vector field correctly</li>
</ul>

<p>Here's a picture... NOTE: the output from the input function strings in the console, these are test arrows, completely unrelated to the function that was input</p>
![phase_1_pic](https://user-images.githubusercontent.com/50467171/159381755-943230be-6a21-4fb4-8df4-3c040b8ac08a.png)
<img src="https://user-images.githubusercontent.com/50467171/159381755-943230be-6a21-4fb4-8df4-3c040b8ac08a.png"/>

<h3>Ready to start phase 2</h3>
<ul>
  <li>input the differential as a piecewise function, I'm thinking an ampersand to delimit the pieces</li>
  <li>split the pieces of the functions up into a list and integrate each one</li>
  <li>use the initial value to calculate any necessary constants</li>
  <li>display the original functions u(t) and v(t) on the interface</li>
</ul>


<h3>in the future phase 3</h3>
<ul>
  <li>use euler's method to plot the function at each point with a magnitude of deltaT (essentially a taylor series approximation, but only one derivative out at each point for accuracy in change)</li>
  <li>rearrange interface so input function is at top, and swap function input boxes for output labels when testing is complete</li>
</ul>
