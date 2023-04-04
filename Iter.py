import numpy as np
from math import *
import cmath as cm


# перестановка элементов уравнения для удобства
# чтоб в n-ной строке у x_n был больший коэффициент
def Recombinate(A, B):
    n = A.shape[0]
    A1 = np.zeros(A.shape)
    B1 = np.zeros(B.shape)
    for i in range(n):
        index = np.argmax(A[i])
        A1[index] = np.copy(A[i])
        B1[index] = np.copy(B[i])
    return A1, B1


def result(A, B, eps):
    n = B.shape[0]
    A, B = Recombinate(A, B)
    # (sum(abs(A[i]))-abs(A[i,i])) - сумма вех элементов i-той строки без i итого элемента
    q = max([(sum(abs(A[i])) - abs(A[i, i])) / abs(A[i, i]) for i in range(n)])
    x = np.array([B[i] / A[i, i] for i in range(n)])
    delta = eps + 1
    itter = 0
    while delta > eps:
        itter += 1
        x_new = np.zeros(n)
        for i in range(n):
            x_new[i] = (B[i] - sum(A[i] * x) + A[i, i] * x[i]) / A[i][i]
        delta = max([q / (1 - q) * abs(x_new[i] - x[i]) for i in range(n)])
        x = np.copy(x_new)
    return x, itter
