import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)

# funcao
def f(t):
    v0 = 1. 
    a = 0.1
    return v0*t + (a*(t**2))/2
def f2(t):
    v0 = 1. 
    a = 0.4
    return v0*t + (a*(t**2))/2

# primeira derivada, DFC
def Df(f,t):
    dt = t[1]-t[0]
    tp = t+dt
    tm = t-dt
    return (f(tp)-f(tm))/(2*dt)

# segunda derivada, DFC
def D2f(f,t):
    dt = t[1]-t[0]
    tp = t+dt
    tm = t-dt
    return (f(tp)-2.*f(t) + f(tm))/(dt*dt)

def Df2(f2,t):
    dt = t[1]-t[0]
    tp = t+dt
    tm = t-dt
    return (f2(tp)-f2(tm))/(2*dt)

# segunda derivada, DFC
def D2f2(f2,t):
    dt = t[1]-t[0]
    tp = t+dt
    tm = t-dt
    return (f2(tp)-2.*f2(t) + f2(tm))/(dt*dt)

n = 64
t = np.linspace(0.,10.,n)
a = f(t)
b = f2(t)
plt.plot(t,a,f2(t), label =r"f(t)")
plt.plot(t,Df(f,t),Df2(f2,t), label =r"f1(t)")
plt.plot(t,D2f(f,t),D2f2(f2,t), label  =r"f2(t)")
ax.legend(loc=2) 
plt.show()
