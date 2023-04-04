import numpy as np
from math import *

def decomp(A):
    n = A.shape[0];
    L = np.zeros((A.shape)) 
 
    L[0] = A[0]/sqrt(A[0][0])
    for i in range(1,n):
        L[i][i] = sqrt(A[i][i] - (L[:,i]**2).sum())
        for j in range(i+1, n):
            L[i][j] = (A[i][j] - (L[:i,i]*L[:i,j]).sum())/L[i][i]
    return L 

def result(L,B):
    n = L.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)
    y[0] = B[0]/L[0][0] 
    for i in range(1,n):
        y[i] = (B[i]-(L[:i,i]*y[:i]).sum())/L[i][i] 
    
    x[n-1] = y[n-1]/L[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - (L[i,i+1:]*x[i+1:]).sum())/L[i][i]    
    
    return x
    
A = np.array([[4,3,0],
                   [3,4,0],
                   [0,0,4]])

B = np.array([7,7,-4])

