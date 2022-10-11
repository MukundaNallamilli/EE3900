import numpy as np
import scipy
import matplotlib.pyplot as plt
def xn(n):
    if n<0:
        return 0
    if 0<=n<=1:
        return 1
    else:
        return xn(n-1)+xn(n-2)
def yn(n):
	return xn(n-1)+xn(n+1)
n=np.arange(10)
vec_xn=scipy.vectorize(xn)
vec_yn=scipy.vectorize(yn)

plt.stem(n,vec_yn(n))
plt.xlabel("n")
plt.ylabel("y(n)")
plt.grid()
plt.savefig("../figs/2_5.png")
plt.show()