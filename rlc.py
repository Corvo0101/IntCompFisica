import math
import cmath
from cmath import sqrt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

L = complex(1000.0)  #Indutancia
C = complex(1.0/1000.0) #Capaciatancia

# 1 - Para R=1000/1.5  e =1/LC, plote na mesma figura a corrente, I e a voltagem V como funcao do tempo.
R = 1000.0/1.5 #resistencia
w = complex(1/sqrt(L*C))
Z = complex(R,((1/w*C)-w*L))
V0 = 1 #Diferença de Potencial 0
I0 = 1 #Corrente 0
x = np.linspace(1,10,10)

a = np.linspace(complex(0,),complex(10,0),100)
b = np.linspace(complex(0,),complex(10,0),100)


for t in range(0,100,1):
  V = V0*cmath.exp(complex(0,w*t))
  I = (1/Z)*V0*cmath.exp(complex(0,-w*t)) 
  a[t] = V
  b[t] = I


plt.plot(a,b)
plt.xlabel('V')
plt.ylabel('I')
plt.show()

