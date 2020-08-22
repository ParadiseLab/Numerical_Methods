import numpy as np



#TODO add doc + add multiple root finding
def newton(function, derivative, x0, max_depth=10,  eps=1e-10):
    x=x0
    i=0
    while i < max_depth: 
        if (derivative(x)==0):
            print("Singularity at x={}".format(x))
        if np.abs(function(x))<=eps:
            return x
        x=x-function(x)/derivative(x)
        i=i+1
    return x



# Find the third root of 27
f = lambda x : 1/3*np.log(27)-np.log(x)
Df = lambda x : -1/x
x = newton(f, Df, 2, 5)
print("The third root of 27 is : {}".format(x))

# Find the the golden ratio
f = lambda x : x**2-x-1
Df = lambda x : 2*x -1
x = newton(f, Df, 4, 6)
print("The golden ratio is : {}".format(x))

# Find the the super golden ratio
f = lambda x : x**3-x**2-1
Df = lambda x : 3*x**2-2*x
x = newton(f, Df, 4, 6)
print("The super golden ratio is : {}".format(x))

# Unprecise function choice
# Find the the value of pi
f = lambda x : np.cos(x)
Df = lambda x : -np.sin(x)
x = newton(f, Df, 1.55, 1000, 1e-10)
print("The value of pi is : {}".format(2*x))
