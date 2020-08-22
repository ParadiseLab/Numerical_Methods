import numpy as np

def dichoto(function, p0, max_depth=10,  eps=1e-10):
    a,b=p0
    i=0
    while i < max_depth:
        c=0.5*(a+b) 
        if np.abs(function(c))<=eps:
            return c
        if(function(c)<0):
            a=c  
        if(function(c)>0):
            b=c
        i=i+1
    return c


# Find the the golden ratio
f = lambda x : x**2-1-x
x = dichoto(f, (1, 2))
print("The golden ratio is : {}".format(x))

# Find the the solution
f = lambda x : np.tan(x)-1
x = dichoto(f, (0.5, 3.15/4), )
print("The solution to tan(x)=0.5 is : {}".format(x))

# Find the the solution
f = lambda x : (x-2)**2
x = dichoto(f, (1, 3), )
print("The solution to (x-2)^2=0 is : {}".format(x))