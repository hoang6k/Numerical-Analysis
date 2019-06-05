import cmath
import numpy as np

A = [[1., 3., -2., 0., -2.],
     [3., 4., -5., 1., -3.],
     [-2., -5., 3., -2., 2.],
     [0., 1., -2., 5., 3.],
     [-2., -3., 2., 3., 4.]]
b = [[0.5], [5.4], [5.0], [7.5], [3.3]]

def cholesky_dec(A):
    n = len(A)
    A = np.asarray(A)
    U = np.zeros((n,n), dtype=complex)
    for i in range(n):
        for j in range(n):
            if i == j:
                U[i,i] = cmath.sqrt(A[i,i] - np.sum(U[0:i,i]**2))
            elif i < j:
                U[i,j] = (A[i,j] - np.sum(U[0:i,i]*U[0:i,j])) / U[i,i]
    return U, U.T

def lower_tri(L, b):
    n = len(L)
    b = np.asarray(b)
    y = np.zeros((n,1), dtype=complex)
    for i in range(n):
        y[i,0] = (b[i,0] - np.sum(L[i,0:i]*y[0:i,0])) / L[i,i]
    return y

def upper_tri(U, y):
    n = len(U)
    x = np.zeros((n,1), dtype=complex)
    for i in range(n-1,-1,-1):
        x[i,0] = (y[i,0] - np.sum(U[i,i+1:]*x[i+1:,0])) / U[i,i]
    return x

U, L = cholesky_dec(A)
y = lower_tri(L, b)
x = upper_tri(U, y)
x = np.asarray(x, dtype=float)
n = len(x)
print('He phuong trinh da cho co nghiem la:')
for i in range(n):
    print('x_{} = {}'.format(i+1, x[i,0]))