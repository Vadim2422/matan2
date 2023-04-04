import numpy as np


def result(A, B):
    n = A.shape[0]
    C = np.zeros(n)
    d = np.zeros(n)
    x = np.zeros(n)

    C[0] = -A[0][1] / A[0][0]
    d[0] = B[0] / A[0][0]
    for i in range(1, n - 1):
        k = A[i][i - 1] * C[i - 1] + A[i, i]
        C[i] = -A[i, i + 1] / k
        d[i] = (B[i] - A[i, i - 1] * d[i - 1]) / k
    C[n - 1] = 0
    d[n - 1] = (A[n - 1][n - 2] * d[n - 2] - B[n - 1]) / (-A[n - 1][n - 1] - A[n - 1][n - 2] * C[n - 2])
    x[n - 1] = d[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = C[i - 1] * x[i] + d[i - 1]
    return x
