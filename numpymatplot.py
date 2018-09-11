import matplotlib
import matplotlib.pyplot as plt
import numpy as np

a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
b = (1,4,9,16,25,36,49,64,81,81,64,49,36,25,16,9,4,1)

x = ('hue','ehu','aj')
y = ('bue','bau','gue')

v = np.array(a)
w = np.array(b)
m = np.array(x)
n = np.array(y)
print(v)
print(w)
print (v+w)
print (v*w)
print(v/w)
print(m)
print(n)

plt.figure()
plt.plot(m,n,'green')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

