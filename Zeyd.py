import numpy as np


def Recombinate(A, B):
    n = A.shape[0]
    A1 = np.zeros(A.shape)
    B1 = np.zeros(B.shape)
    for i in range(n):
        index = np.argmax(A[i])
        A1[index] = np.copy(A[i])
        B1[index] = np.copy(B[i])
    return A1, B1


def result(A, b, eps):
    A, b = Recombinate(A, b)
    n = A.shape[0]
    g = np.zeros(n)
    H = np.zeros(A.shape)

    for i in range(n):
        g[i] = b[i] / A[i][i]

    for i in range(n):
        for j in range(n):
            if i != j:
                H[i][j] = -A[i][j] / A[i][i]

    X = np.zeros(n)
    Xprev = np.zeros(n)

    delta = eps + 1
    itter = 0
    while delta > eps:
        itter += 1
        for i in range(n):
            X[i] = g[i] + H[i].dot(X)

        delta = max([abs(min(X - Xprev)), abs(max(X - Xprev))])
        Xprev = np.copy(X)
    return X, itter
