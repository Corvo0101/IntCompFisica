import matplotlib.pylab as plt
import numpy as np
%matplotlib inline

tempo, posicao, l3,l4,l5 = np.loadtxt('data/edc3deuttemp2007.txt', unpack = True)
plt.plot(l3,l5)
plt.xlabel('tempo')
plt.ylabel('posição')
