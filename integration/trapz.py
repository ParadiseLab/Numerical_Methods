import numpy as np


def trapz(function, p0, n : int):
    x,y=p0
    dx=np.abs(x-y)/n
    r=0
    for i in range(n):
        r=r+(function(x)+0.5*(function(x+dx)-function(x)))*dx
        x=x+dx
    return r


# find the value of pi by integrating sin(x)^2 from 0 to 2pi
f = lambda x : np.sin(x)**2
x = trapz(f, (0, 2*np.pi), int(1e6))
print("The value of pi is : {}".format(x))