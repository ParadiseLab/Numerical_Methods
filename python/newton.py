import numpy as np

def newton(function, derivative, x0, depth=4):
    x=x0
    for i in range(depth) : x=x-function(x)/derivative(x)
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
