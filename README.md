# InitialValueCalculator
A project in a Mathematical Modeling class, number MATH 537 at Indiana State University, was to write a program that solves time dependent ODE's as Initial Value Problems using Euler's Method.


<h3>Phase 1 Complete</h3>
<ul>
  <li>Got the rough plan for the interface together</li>
  <li>User manual being built while each step is being debugged, available under help menu</li>
  <li>It can process the functions when they're given as a string, both continuous and discrete sets</li>
  <li>works with or without a user given delta time (0.1 is the default)</li>
  <li>arrows can be drawn on the vector field correctly</li>
  <li>input the differential as a piecewise function, I'm thinking an ampersand to delimit the pieces</li>
</ul>

<p>Here's a picture... NOTE: the output from the input function strings in the console in the background, the arrows on the vector field are test arrows only and are completely unrelated to the function that was input</p>

<img src="https://user-images.githubusercontent.com/50467171/159381755-943230be-6a21-4fb4-8df4-3c040b8ac08a.png"/>
<img src="https://user-images.githubusercontent.com/50467171/159385072-f7190283-adb8-4881-a603-abb8ca81bff3.png"/>

<br>
<br>

<h3>Phase 2 Complete</h3>
<ul>  
  <li>split the pieces of the functions up into a list and use euler's method to approximate next value</li>
  <li>compare to the original functions u(t) and v(t) on the interface</li>
  <li>get the save and open functions working so I can stop typing a lorenz attractor every test run</li>
</ul>

<p>Here's a picture... NOTE: the output in the console in the background shows the IVP does not align with the original function, no need to graph until they seem close</p>

<img src="https://user-images.githubusercontent.com/50467171/159564987-a7d20cf6-3e1f-4149-bc8d-8e83b98a4d29.png"/>


<h3>in the future phase 3</h3>
<ul>
  <li>use euler's method to plot the function at each point with a magnitude of deltaT (essentially a taylor series approximation, but only one derivative out at each point for accuracy in change)</li>
  <li>rearrange interface so input function is at top, and swap function input boxes for output labels when testing is complete</li>
</ul>
