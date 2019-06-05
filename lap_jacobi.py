import numpy as np

A = [[10., 2., -1., 2.],
     [1., 5., 1., 0.],
     [1., -2., -5., 1.],
     [3., 0., 0., -9.]]
b = [[-4.], [-1.], [2.], [10.]]

def cheo_troi_hang(A, b, eps):
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
    x0 = np.zeros((n,1))
    x1 = alpha.dot(x0) + beta
    x = [x0, x1]
    
    # tinh chuan ma tran va so vong lap
    q = np.around(np.linalg.norm(alpha, ord=float('inf')), decimals=6) + 0.00001
    k = np.around(np.log((1-q)*eps / np.linalg.norm(x1-x0, ord=float('inf'))) / np.log(q)) + 1
    print('norm = ' + str(q))
    print('k = ' + str(int(k)))
    
    # thuc hien them k-1 vong lap
    for i in range(int(k)-1):
        x.append(alpha.dot(x[-1]) + beta)
    return x[-1]

def cheo_troi_cot(A, b, eps):
    n = len(A)
    I = np.identity(n)
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    
    # luu lai mang doi bien
    a_ii = np.asarray([A[i,i] for i in range(n)]).reshape((n,1))
    _a_ii = np.abs(a_ii)
    _lambda = np.max(_a_ii) / np.min(_a_ii)
    for i in range(n):
        A[:,i] = A[:,i] / A[i,i]
    alpha = I - A
    beta = b
#    print(alpha)
#    print(beta)
    x0 = np.zeros((n,1))
    x1 = alpha.dot(x0) + beta
    x = [x0, x1]
    
    # tinh chuan ma tran va so vong lap
    q = np.around(np.linalg.norm(alpha, ord=1), decimals=6) + 0.00001
    k = np.around(np.log((1-q)*eps / (_lambda * np.linalg.norm(x1-x0, ord=1))) / np.log(q)) + 1
    print('norm = ' + str(q))
    print('k = ' + str(int(k)))
    
    # thuc hien them k-1 vong lap
    for i in range(int(k)-1):
        x.append(alpha.dot(x[-1]) + beta)
    return x[-1] / a_ii

eps = 1e-8

X = cheo_troi_hang(A, b, eps)
n = len(X)
print('He phuong trinh da cho co nghiem giai voi cheo troi hang la:')
for i in range(n):
    print('x_{} = {}'.format(i+1, X[i]))

X = cheo_troi_cot(A, b, eps)
n = len(X)
print('He phuong trinh da cho co nghiem giai voi cheo troi cot la:')
for i in range(n):
    print('x_{} = {}'.format(i+1, X[i]))