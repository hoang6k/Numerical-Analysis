import math

def dao_ham(x0):
    a = x0 - 1e-5
    b = x0 + 1e-5
    dht = (f(x0) - f(a)) / (x0 - a)
    dhp = (f(b) - f(x0)) / (b - x0)
    while math.fabs(dhp - dht) > eps:
        a = (a + x0) / 2
        b = (x0 + b) /2
        dht = (f(x0) - f(a)) / (x0 - a)
        dhp = (f(b) - f(x0)) / (b - x0)
    return dht
    
def f(x):
    return x**3

x0 = 1.3
eps = 1e-8
N = 100
deriv_x0 = dao_ham(x0)
print('Ta co dao ham cua f tai x0 = {} la {}'.format(x0, deriv_x0))