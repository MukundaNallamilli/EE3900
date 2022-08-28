def u(n):
    if n <0 :
        return 0.0
    else :
        return 1.0
def h(n):
    return u(n)*(-1.0/2)**n + u(n-2)*(-1.0/2)**(n-2)
sum = 0    
for i in range(4000):
    sum +=h(i)
print(sum)    