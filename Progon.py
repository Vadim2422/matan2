import numpy as np
from math import *
import cmath as cm

def result(A,B):
    n = A.shape[0]
    C = np.zeros(n)
    d = np.zeros(n)
    x = np.zeros(n)
    
    C[0] = -A[0][1]/A[0][0]
    d[0] = B[0]/A[0][0]
    for i in range(1,n-1):
        k = A[i][i-1]*C[i-1] + A[i,i]
        C[i] = -A[i,i+1]/k
        d[i] = (B[i] - A[i,i-1]*d[i-1])/k
    C[n-1] = 0
    d[n-1] = (A[n-1][n-2]*d[n-2] - B[n-1])/(-A[n-1][n-1] - A[n-1][n-2]*C[n-2])
    x[n-1] = d[n-1]
    for i in range(n-1,0,-1):
        x[i-1] = C[i-1]*x[i] + d[i-1] 
    return x

A = np.array([
    [4,2,0,0],
    [1,8,2,0],
    [0,1,9,1],
    [0,0,2,4]
])

B = np.array([3,11,11,6])
