import math
import cmath
from cmath import sqrt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

L = complex(1000.0)  #Indutancia
C = complex(1.0/1000.0) #Capacitancia

# 1 - Para R=1000/1.5  e =1/LC, plote na mesma figura a corrente, I e a voltagem V como funcao do tempo.
R = 1000.0/1.5 #resistencia
w = complex(1/sqrt(L*C))
Z = complex(R,((1/w*C)-w*L))
V0 = 1 #Diferença de Potencial 0
I0 = 1 #Corrente 0

a = np.linspace(complex(0.),complex(10,0),100)
b = np.linspace(complex(0.),complex(10,0),100)

def quest1():
  for t in range(0,100,1):  
    V = V0*cmath.exp(complex(0,w*t))
    I = (1/Z)*V0*cmath.exp(complex(0,-w*t)) 
    a[t] = V
    b[t] = I
  plt.plot(a,b)
  plt.xlabel('V')
  plt.ylabel('I')
  plt.show()    
    

#2 - Para tres valores diferentes da resistencia, R=1000/1.5,1000/2e1000/5.2, faça um gráfico de 1/|Z| vs w, para 0<w<2/LC. Utilize as funções np.max() e np.min() para determinar o valor da frequencia de resonancia.

R1 = R
R2 = 1000.0/2.0
R3 = 100.0/5.2
i = 1

def quest2R1():# R1
  i = 1   
  while i !=(2/cmath.sqrt(L*C)):
    contador = 1  
    w = 2/(i*cmath.sqrt(C*L))
    mZ = cmath.sqrt(R1**2 + (((1/w*C)-w*L)**2)) #Modulo de Z
    a[contador] = 1/mZ
    b[contador] = w
    i+=0.5
    contador+=1  
  plt.plot(a,b)
  plt.xlabel('V')
  plt.ylabel('I')
  plt.show()    

def quest2R2(): #R2
  i = 1 
  while i !=(2/cmath.sqrt(L*C)):
    contador = 1  
    w = 2/(i*cmath.sqrt(C*L))
    mZ = cmath.sqrt(R2**2 + (((1/w*C)-w*L)**2)) #Modulo de Z
    a[contador] = 1/mZ
    b[contador] = w
    i+=0.5
    contador+=1  
  plt.plot(a,b)
  plt.xlabel('V')
  plt.ylabel('I')
  plt.show()    

#R3
def quest2R3(): 
  i = 1   
  while i !=(2/cmath.sqrt(L*C)):
    contador = 1  
    w = 2/(i*cmath.sqrt(C*L))
    mZ = cmath.sqrt(R2**2 + (((1/w*C)-w*L)**2)) #Modulo de Z
    a[contador] = 1/mZ
    b[contador] = w
    i+=0.5
    contador+=1  
  plt.plot(a,b)
  plt.xlabel('V')
  plt.ylabel('I')
  plt.show()    

def menu():    
  opc = 0
  while opc != -1:
    opc = int(input())
    if opc == 1:
      quest1()
    if opc == 2:
      quest2R1()
    if opc == 3:
      quest2R2()
    if opc == 4:
      quest2R3()
    if opc == 5:
      opc = -1
    opc = -1            

menu()
    
