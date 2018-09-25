import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math


# PROGRAMA PARA CALCULAR PRIMEIRA E SEGUNDA DERIVADA DA 
# FUNCAO ARBITRARIA f(x)

# funcao
def f(x):
    return np.cos(x)

# primeira derivada, DFC
def Df(f,x):
    dx = x[1]-x[0]
    xp = x+dx
    xm = x-dx
    return (f(xp)-f(xm))/(2*dx)

# segunda derivada, DFC
def D2f(f,x):
    dx = x[1]-x[0]
    xp = x+dx
    xm = x-dx
    return (f(xp)-2.*f(x) + f(xm))/(dx*dx)
#erro

def Erro(f,x):
    e = np.sqrt((((D2f(f,x)-f(x))/f(x))**2))
    return e


n = 64
x = np.linspace(0.,10.,n)
a = f(x)
#plt.plot(x,a)
#plt.plot(x,Df(f,x))
plt.plot(x,D2f(f,x), label = "D2f")
plt.plot(x,D2f(f,x)+Erro(f,x),label = "D2f + e")
plt.legend()
