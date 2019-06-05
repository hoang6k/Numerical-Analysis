import numpy as np

#A = [[7.9, 5.6, 5.7, -7.2],
#     [8.5, -4.8, 0.8, 3.5],
#     [4.3, 4.2, -3.2, 9.3],
#     [3.2, -1.4, -8.9, 3.3]]
#b = [[6.68], [9.95], [8.6], [1.0]]

A = [[10., 2., -1., 2.],
     [1., 5., 1., 0.],
     [1., -2., -5., 1.],
     [3., 0., 0., -9.]]
b = [[-4.], [-1.], [2.], [10.]]

def gauss(A, b):
    Ab = np.concatenate((A, b), axis=1)
    print(Ab)
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            Ab[j,i:] = Ab[j,i:] - Ab[j,i] * Ab[i,i:] / Ab[i,i]
    print(Ab)
    X = np.zeros((n, 1))
    X[n-1] = Ab[n-1, n] / Ab[n-1, n-1]
    for i in range(n-2, -1, -1):
        X[i] = (Ab[i,-1] - Ab[i,i+1:n].dot(X[i+1:n])) / Ab[i,i]
    return X

X = gauss(A, b)
n = len(X)
print('He phuong trinh da cho co nghiem la:')
for i in range(n):
    print('x_{} = {}'.format(i+1, X[i]))