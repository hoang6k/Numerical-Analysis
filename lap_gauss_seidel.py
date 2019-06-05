import numpy as np

A = [[10., 2., -1., 2.],
     [1., 5., 1., 0.],
     [1., -2., -5., 1.],
     [3., 0., 0., -9.]]
b = [[-4.], [-1.], [2.], [10.]]

def iteration(alpha, beta, x):
    n = len(x)
    x_new = []
    for i in range(n):
        print(alpha[i,:i])
        print(np.asarray(x_new))
        print(alpha[i,i+1:])
        print(x[i+1:,0])
        x_new.append(np.sum(alpha[i,:i]*np.asarray(x_new)) + 
                     np.sum(alpha[i,i+1:]*x[i+1:,0]) + beta[i,0])
    return np.asarray(x_new).reshape((n,1))

def gauss_seidel(A, b, eps):
    n = len(A)
    I = np.identity(n)
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    for i in range(n):
        b[i,0] = b[i,0] / A[i,i]
        A[i,:] = A[i,:] / A[i,i]
    alpha = I - A
    beta = b
#    print(alpha)
#    print(beta)
    
    # tinh he so sai so u
    p = []
    q = []
    for i in range(n):
        p.append(1-np.sum(np.abs(alpha[i,:i])))
        q.append(np.sum(np.abs(alpha[i,i+1:])))
    u = np.max(np.asarray(q) / np.asarray(p))
    print('u = ' + str(u))
    
    x0 = beta
    x1 = iteration(alpha, beta, x0)
    x = [x0, x1]
    print(x0)
    print(x1)
    while u/(1-u) * np.linalg.norm(x[-1]-x[-2], ord=float('inf')) > eps:
        x.append(iteration(alpha, beta, x[-1]))
    print('k = ' + str(len(x)-1))
    return x[-1]

eps = 1e-8

X = gauss_seidel(A, b, eps)
n = len(X)
print('He phuong trinh da cho co nghiem la:')
for i in range(n):
    print('x_{} = {}'.format(i+1, X[i]))