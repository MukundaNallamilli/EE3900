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

def f4(n,a,b):
    return a**n+b**n

vec_bn=scipy.vectorize(bn)
vec_f4=scipy.vectorize(f4)
l4=vec_bn(n,a,b)
l5=vec_f4(n,a,b)


plt.subplot(211)
plt.plot(n,l4,label=r'$b_{n}$',color='r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(n,l5,label=r'$\alpha^n+\beta^n$')
plt.grid()
plt.legend()
plt.savefig('../figs/1_3.png')
plt.show()