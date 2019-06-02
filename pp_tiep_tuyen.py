import math
from sympy import Symbol, Derivative

def tim_nghiem(f, x, a, b, eps=1e-8, N=1000): #gia su ham f tren (a,b) la loi hoac lom
    iter = 1
    deriv = Derivative(f, x).doit()
    deriv_a = deriv.subs({x:a})
    deriv_b = deriv.subs({x:b})
    nd_deriv = Derivative(deriv, x).doit()
    nd_deriv_a = nd_deriv.subs({x:a})
    nd_deriv_b = nd_deriv.subs({x:b})
    m = min([deriv_a, deriv_b])
    M = max([deriv_a, deriv_b])
    
    #kiem tra dieu kien
    if deriv_a*deriv_b < 0 or nd_deriv_a*nd_deriv_b< 0:
        return float('NaN'), 0
    
    #tim xap xi ban dau x0
    if f.subs({x:a})*nd_deriv_a > 0:
        x0 = a
    else:
        x0 = b
    x_n_1 = x0
    x_n = x_n_1 - f.subs({x:x_n_1}) / deriv.subs({x:x_n_1})
    print('iter = {}: x_n = {}'.format(iter, x_n))
    while math.fabs(x_n - x_n_1) > math.sqrt(2*m*eps/M):
        x_n_1 = x_n
        x_n = x_n_1 - f.subs({x:x_n_1}) / deriv.subs({x:x_n_1})
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