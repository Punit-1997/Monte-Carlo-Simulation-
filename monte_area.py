"""
Title : Area of circle by using monte-carlo method :
      
"""
import numpy as np 
import random 

# Input Parameter
R=2.0  #radius 
N=10000 # Total number of ittrartion 
count=0
z=np.random.uniform(-R, R)
for i in range(N):
    x=np.random.uniform(-R,R)
    y=np.random.uniform(-R,R)
    r=np.sqrt(x**2 + y**2)
    if (r<=R):
        count=count+1
Area_Sq =4*R*R          # area of square 
Area_circle = Area_Sq*count/N
print(Area_circle)