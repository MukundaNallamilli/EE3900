import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

n=np.arange(1,100)

def an(n,a,b):
    if n<=0:
        return 0.0
    else:
        return (a**n-b**n)/(a-b)
vec_an=scipy.vectorize(an)

def bn(n,a,b):
    if n>=1:
        return an(n-1,a,b)+an(n+1,a,b)
    else:
        return 0.0

def f1(n,a,b):
    return an(n+2,a,b)-1

a=(1+math.sqrt(5))/2
b=(1-math.sqrt(5))/2

def f3(n,a,b):
   return np.dot(vec_an(np.arange(n),a,b),np.array([1/10**i for i in range(n)]))-10/89

vec_f3=scipy.vectorize(f3)
l3=vec_f3(n,a,b)

plt.plot(n,l3,label=r'$\sum_{k=1}^{n}\frac{a_{k}}{10^k}-(\frac{10}{89})$',color='r')
plt.legend()
plt.grid()
plt.savefig('../figs/1_2.png')
plt.show()