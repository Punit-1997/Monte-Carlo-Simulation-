# Monte-Carlo-Simulation-
#### Overview of The Repository :
I made this repository for beginner who want to learn Monte - Carlo on your own.This repository help in basic understanding of method and there applicability in the real life problem. I mostly cover the application of monte carlo in different areas Physics such as classical mechanics, quantum mechanics, statistical mechanics,but there monte carlo method can be use to model various physical process.
##### Prerequisite for the course:
Basic background in programing skill is enough for learning monte carlo user can choose any languge as per there preference. I will use fortran 90 as programing language for this purpose but user can use any language.
###### Basic Outline of Course : 
Basic of Monte Carlo 

###### There are many example where we can apply the Monte-Carlo Method here we will understand it by demonstrating following example.
###### 1. To calculate area of circle 
###### 2.1D Random walk problem 
###### 3.Totalty assymetric model 
###### 4.2D ising spin model
###### 5.1D Molecular Dyanamics

###### Calculation of Area of cicle:

The formula to find the area of a circle is πr^2, where r is the radius of the circle. 
So if a circle has radius r = 1, its area is π. The formula to find the area of a square is s^2, where s is the side length of the square.
Let’s use a Monte Carlo method to compute area of circle. We will look at circle inscribed in a square with side length 2.
The area of the square is (2*R)^2 ie equal to 16, and the area of the circle is π*r^2 is equal to 12.56.
So if you dropped a grain of sand in the square, it has a probability of droping the grain in circle will be 
###### P(grain inside circle) = (Area of circle)/(Area of square) = (Number of grain in circle)/(Number of grain in square)
###### Area of circle = (Number of grain in circle)*(Area of square)/(Number of grain in square)
