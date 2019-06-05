import cmath
import numpy as np

A = [[1., 3., -2.],
     [3., 4., -5.],
     [-2., -5., 3.]]

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

def inv_cholesky(A):
    n = len(A)
    U, L = cholesky_dec(A)
    U_1 = np.zeros((n,n), dtype=complex)
    for i in range(n-1, -1, -1):
        U_1[i,i] = 1. / U[i,i]
        for j in range(i+1,n):
            U_1[i,j] = np.sum(-U[i,i+1:] * U_1[i+1:,j] / U[i,i])
    return U_1.dot(U_1.T)

print("Ma tran A la:")
print(np.asarray(A))
A_1 = inv_cholesky(A)
print("Ma tran nghich dao cua A la:")
print(A_1.real)