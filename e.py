import numpy as np

eps = 1e-8
i = 1
n_fac = 1
e_n = 1
e_n_1 = 0
iter = 0
while e_n - e_n_1 > eps:
    n_fac *= i
    i += 1
    e_n_1 = e_n
    e_n += 1.0 / n_fac
    iter += 1

print('sau {} vong lap, e = {}'.format(iter, e_n))