import numpy as np 

def decomp(A):
    n = A.shape[0];
    L = np.zeros([n,n])
    U = np.eye(n)
    L[:,0] = A[:,0]
    U[0,1:] = A[0,1:]
    U[0,1:] /= L[0,0]

    for j in range(1,n):
        for i in range(1,n):
            if(i>=j):
                L[i][j] = A[i][j]-(L[i,:j]*U[:j,j]).sum()
            if(i<j):
                U[i][j] = (A[i][j]-(L[i,:i]*U[:i,j]).sum())/L[i][i]
    return L, U


def result(L, U, B):
    n = U.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)
    y[0] = B[0]/L[0][0] 
    for i in range(1,n):
        y[i] = (B[i]-(L[i,:i]*y[:i]).sum())/L[i][i] 
    
    x[n-1] = y[n-1]
    for i in range(n-2, -1, -1):
        tmp = 0
        for k in range(i+1,n): tmp += U[i,k]*x[k]
        x[i] = y[i]-tmp
    return x


A = np.array([[4,2,1],[1,5,0],[3,1,8]])
B = np.array([1,-4,-6])
