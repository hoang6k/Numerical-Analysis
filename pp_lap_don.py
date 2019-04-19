import math

def tim_nghiem(a, b, q, eps=1e-8, N=1000):
    iter = 1
    x0 = (a + b) / 2
    x_n_1 = x0
    x_n = f(x_n_1)
    while q/(1-q) * math.fabs(x_n - x_n_1) > eps:
        x_n_1 = x_n
        x_n = f(x_n)
        iter += 1
        print('iter = {}: x_n = {}'.format(iter, x_n))
    return x_n, iter

def f(x):
    return (x+1)**(1/5)

a = 1
b = 2
q = 1/5
eps = 1e-8
N = 100
x0, iter = tim_nghiem(a, b, q, eps, N)
print('Ta co nghiem sau {} vong lap la x0 = {}'.format(iter, x0))