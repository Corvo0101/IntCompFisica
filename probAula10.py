import numpy as np
import math as mt
d1 = 2.6+3.7+1.5
d2 = 1.5
d3 = 3.7+1.5
A = np.array([[mt.sin(mt.radians(69.3)),mt.sin(mt.radians(71.1)),mt.sin(mt.radians(56.6))],[mt.cos(mt.radians(69.3)),mt.cos(mt.radians(71.1)),mt.cos(mt.radians(56.6))],[d1, d2, d3]])
Fr = np.array([926, 0, 0])

LU = scipy.linalg.lu_factor(A)

n=3
I = np.zeros_like(A)
for i in range (n):
    I[i,i] = 1.
    
    
Ainv = scipy.linalg.lu_solve(LU,I)
