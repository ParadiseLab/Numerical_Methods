import numpy as np


def simpson(function, p0, n : int):
    x,y=p0
    dx=np.abs(x-y)/n
    r=0
    for i in range(n):
        r=r+(1/6)*(x+dx-x)*(function(x)+function(x+dx)+4*function(x+dx/2))
        x=x+dx
    return r


# find the value of pi by integrating sin(x)^2 from 0 to 2pi
f = lambda x : np.sin(x)**2
x = simpson(f, (0, 2*np.pi), int(1e6))
print("The value of pi is : {}".format(x))