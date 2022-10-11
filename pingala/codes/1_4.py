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
def bn(n,a,b):
    if n>=1:
        return an(n-1,a,b)+an(n+1,a,b)
    else:
        return 0.0

def f1(n,a,b):
    return an(n+2,a,b)-1
a=(1+math.sqrt(5))/2
b=(1-math.sqrt(5))/2

vec_bn=scipy.vectorize(bn)
def f5(n,a,b):
   return np.dot(vec_bn(np.arange(n),a,b),np.array([1/10**i for i in range(n)]))-8/89
vec_f5=scipy.vectorize(f5)

l6=vec_f5(n,a,b)
plt.plot(n,l6,label=r'$\sum_{k=1}^{n}\frac{b_{k}}{10^k}-(\frac{8}{89})$')
plt.grid()
plt.legend()
plt.savefig('../figs/1_4.png')
plt.show()