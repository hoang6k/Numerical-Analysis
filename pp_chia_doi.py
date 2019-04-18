import numpy as np
from scipy.misc import derivative

def tim_nghiem(a, b, eps=1e-8, N=1000):
    iter = 0
    while b-a > 2*eps and iter < N:
        x0 = (a+b)/2.0
        if f(a)*f(x0) > 0:
            a = x0
        else:
            b = x0
        iter += 1
#        print('iter = {}: x0 = {}'.format(iter, x0))
    return x0, iter
    
def f(x):
    return x**3 - 3*x

a = 1.6
b = 1.8
eps = 1e-8
N = 100
x0, iter = tim_nghiem(a, b, eps, N)
print('Ta co nghiem sau {} vong lap la x0 = {}'.format(iter, x0))