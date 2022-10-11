import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

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

n=np.arange(1,100)
vec_an=scipy.vectorize(an)

# summation of ak 
def f2(n,a,b):
    return np.sum(vec_an(np.arange(n),a,b))


vec_f1=scipy.vectorize(f1)
vec_f2=scipy.vectorize(f2)
l1=vec_f1(n,a,b)
l2=vec_f2(n,a,b)

plt.subplot(211)
plt.plot(n,l1,label=r'$a_{n+2}-1$',color='r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(n,l2,label=r'$\sum_{k=1}^{n}a_{k}$')
plt.grid()
plt.legend()
plt.savefig('../figs/1_1.png')
plt.show()


