import numpy as np
# from v_matrix import *
from l_matrix import *
from math import *
import cmath as cm

import Gaus
import LU
import LLT
import Progon
import Iter
import Zeyd



def Newyazka(A,B,X):
    Bruh = np.array([sum(A[i]*X) for i in range(A.shape[0])])
    result = sqrt(sum((B-Bruh)**2))
    return result

print("Классический метод Гаусса")
X = Gaus.result(np.copy(A1), np.copy(B1))
print("Гаус1 простой X:", X, "   ||B-B\'|| = ", Newyazka(A1, B1, X))
X = Gaus.result(np.copy(A2), np.copy(B2))
print("Гаус2 простой X:", X, "   ||B-B\'|| = ", Newyazka(A2, B2, X))
X = Gaus.result(np.copy(A3), np.copy(B3))
print("Гаус3 простой X:", X, "   ||B-B\'|| = ", Newyazka(A3, B3, X))
print()

print("Метод Гаусса с частичным выбором главного элемента")
X = Gaus.result_nofull(np.copy(A1), np.copy(B1))
print("Гаус1 частичный X:", X, "   ||B-B\'|| = ", Newyazka(A1, B1, X))
X = Gaus.result_nofull(np.copy(A2), np.copy(B2))
print("Гаус2 частичный X:", X, "   ||B-B\'|| = ", Newyazka(A2, B2, X))
X = Gaus.result_nofull(np.copy(A3), np.copy(B3))
print("Гаус3 частичный X:", X, "   ||B-B\'|| = ", Newyazka(A3, B3, X))
print()

print("Метод Гаусса с полным выбором главного элемента")
X = Gaus.result_full(np.copy(A1), np.copy(B1))
print("Гаус1 полный X:", X, "   ||B-B\'|| = ", Newyazka(A1, B1, X))
X = Gaus.result_full(np.copy(A2), np.copy(B2))
print("Гаус2 полный X:", X, "   ||B-B\'|| = ", Newyazka(A2, B2, X))
X = Gaus.result_full(np.copy(A3), np.copy(B3))
print("Гаус3 полный X:", X, "   ||B-B\'|| = ", Newyazka(A3, B3, X))
print()



L,U = LU.decomp(A2)
X = LU.result(L,U,B2)
print("LU X:", X, "   ||B-B\'|| = ", Newyazka(A2, B2, X))
print()

L = LLT.decomp(A2)
X = LLT.result(L,B2)
print("LLT X:", X, "   ||B-B\'|| = ", Newyazka(A2, B2, X))
print()

X = Progon.result(A3, B3)
print("Прогонка X:", X, "   ||B-B\'|| = ", Newyazka(A3, B3, X))
print()

A = np.copy(A1)
B = np.copy(B1)
X,itter = Iter.result(A, B, 0.001)
print("Итерация X:", X, "   ||B-B\'|| = ", Newyazka(A, B, X))
print("колличество иттераций: ", itter)
print()

A = np.copy(A1)
B = np.copy(B1)
X,itter = Zeyd.result(A, B, 0.001)
print("Зейдель  X:", X, "   ||B-B\'|| = ", Newyazka(A, B, X))
print("колличество иттераций: ", itter)
