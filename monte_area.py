"""
Title : Area of circle by using monte-carlo method :
Outline : 1. First define initial parameter 
          2. generate the random number inside the square and count how many are 
"""
import numpy as np 
import random 
import matplotlib.pyplot as plt

# Input Parameter
R=2.0  #radius 
N=1000  #Total number of ittrartion 
count=0
x1=np.zeros(N,dtype=float)
y1=np.zeros(N,dtype=float)
for i in range(N):
    x=np.random.uniform(-R,R)
    y=np.random.uniform(-R,R)
    x1[i]=x
    y1[i]=y
    r=np.sqrt(x**2 + y**2)
    if (r<=R):
        count=count+1
Area_Sq =4*R*R          # area of square 
Area_circle = Area_Sq*count/N
print(Area_circle)

plt.scatter(x1,y1)
plt.xlim(-2,2)
plt.ylim(-2,2)


# to generate the cicle inside square of length 2*R
theta = np.linspace( 0 , 2 * np.pi , 150 )
 
radius = 2
 
a = radius * np.cos( theta )
b = radius * np.sin( theta )
plt.plot(a,b,'r')