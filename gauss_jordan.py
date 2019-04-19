import numpy as np

A = [[7.9, 5.6, 5.7, -7.2],
     [8.5, -4.8, 0.8, 3.5],
     [4.3, 4.2, -3.2, 9.3],
     [3.2, -1.4, -8.9, 3.3]]
b = [[6.68], [9.95], [8.6], [1.0]]

def gauss(A, b):
    Ab = np.concatenate((A, b), axis=1)
    print(Ab)
    n = len(A)
    for i in range(n):
        idx_max = np.argmax(np.abs(Ab[i:,i]))
        Ab[[i,i+idx_max]] = Ab[[i+idx_max,i]]
        Ab[i,:] = Ab[i,:] / Ab[i,i]
        for j in range(n):
            if j == i:
                continue
            Ab[j, i+1:] = Ab[j,i+1:] - Ab[j,i] * Ab[i,i+1:]
            Ab[j,i] = 0
        print(Ab)
    return Ab[:,-1]

X = gauss(A, b)
n = len(X)
print('He phuong trinh da cho co nghiem la:')
for i in range(n):
    print('x_{} = {}'.format(i+1, X[i]))