import math

eps = 1e-8
i = 1
x5 = 1/5
x239 = 1/239
arctan5 = 1/5
arctan239 = 1/239
pi_n = 0
pi_n_1 = -1
iter = 0

while math.fabs(pi_n - pi_n_1) > eps:
    x5 *= - 1/5**2 * i/(i+2)
    x239 *= - 1/239**2 * i/(i+2)
    arctan5 += x5
    arctan239 += x239
    pi_n_1 = pi_n
    pi_n = 16*arctan5 - 4*arctan239
    i += 2
    iter +=1
    print(pi_n)

print('sau {} vong lap, pi = {}'.format(iter, pi_n))
