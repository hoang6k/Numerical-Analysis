import numpy as np

A = [[50., 107., 36.],
     [25., 54., 20.],
     [31., 66., 21.]]

def inv_gauss_jordan(A):
    n = len(A)
    A = np.asarray(A)
    E = np.identity(n)
    AE = np.concatenate((A,E), axis=1)
#    print(AE)
    for i in range(n):
        AE[i] = AE[i] / AE[i,i]
        for j in range(n):
            if j!=i:
                AE[j] = AE[j] - AE[j,i]*AE[i]
#    print(AE)
    return AE[:,n:]

print("Ma tran A la:")
print(np.asarray(A))
A_1 = inv_gauss_jordan(A)
print("Ma tran nghich dao cua A la:")
print(A_1)