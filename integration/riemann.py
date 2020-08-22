import numpy as np


def riemann(function, p0, n : int):
    x,y=p0
    dx=np.abs(x-y)/n
    r=0
    for i in range(n):
        r=r+function(x)*dx
        x=x+dx
    return r


# find the value of pi by integrating sin(x)^2 from 0 to 2pi
f = lambda x : x**2*np.cos(x)
x = riemann(f, (0, np.pi), int(1e6))
print("The value of pi is : {}".format(x))