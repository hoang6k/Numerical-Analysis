import math
from sympy import Symbol, Derivative

def tim_nghiem(f, x, a, b, eps=1e-8, N=1000): #gia su ham f tren (a,b) la loi hoac lom
    iter = 0
    deriv = Derivative(f, x).doit()
    deriv_a = deriv.subs({x:a})
    deriv_b = deriv.subs({x:b})
    m = min([deriv_a, deriv_b])
    
    x1 = f.subs({x:a}) - f.subs({x:a}) / deriv_a
    if x1 > a and x1 < b:
        x0 = a
    else:
        x0 = b
    x_n = x0
    while math.fabs(f.subs({x:x_n})) / m > eps:
        x_n = x_n - f.subs({x:x_n}) / deriv.subs({x:x_n})
        iter += 1
        print('iter = {}: x_n = {}'.format(iter, x_n))
    return x_n, iter
    
n = 5
A = 19
x = Symbol('x')
f = x**n - A

a = 1.6
b = 2.0
eps = 1e-8
N = 100
x0, iter = tim_nghiem(f, x, a, b, eps, N)
print('Ta co nghiem sau {} vong lap la x0 = {}'.format(iter, x0))