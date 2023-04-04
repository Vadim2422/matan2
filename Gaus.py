import numpy as np
from math import *
import cmath as cm

def back_move(A,B):
    n = A.shape[0] 
    x = np.zeros(n)
    x[n-1] = B[n-1]/A[n-1, n-1]
    for i in range(n-2,-1,-1):
        x[i] = (B[i] - (A[i,i+1:]*x[i+1:]).sum())/A[i,i]
    return x

# поиск максимума в столбце
def search_max_line(A):
    index = 0
    for i in range(A.shape[0]):
        if abs(A[i])>abs(A[index]):
            index = i
    return index
# поиск максимума среди всех элементов
def search_max(A):
    index = [0,0]
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if abs(A[index[0],index[1]]) < abs(A[i,j]):
                index = [i,j]
    return index



# обычный метод гаусса
def result(A,B):
    n = A.shape[0] 
    for i in range(n-1):
        for y in range(i+1,n):  # вычитаем из всего i-тую строку
            delta = A[y,i]/A[i,i]
            A[y,i:] = A[y,i:] - A[i,i:]*delta
            B[y] = B[y] - B[i]*delta
    
    out = back_move(A,B)
    return out

# метод гауса с выбором главного элемента
def result_full(A,B):
    n = A.shape[0] 
    save = np.array([i for i in range(n)])
    # переставляем чтоб максимумы по диагонали шли
    for i in range(n-1):
        index = search_max(A[i:,i:])
        index[0] += i; index[1] += i;

        tmp_s = save[i]
        save[i] = save[index[1]]
        save[index[1]] = tmp_s
        
        tmp = np.copy(A[:,index[1]])
        A[:,index[1]] = np.copy(A[:,i])
        A[:,i] = np.copy(tmp[:])
        A[[index[0], i]] = A[[i, index[0]]]
        
        tmp1 = B[index[0]]
        B[index[0]] = B[i]
        B[i] = tmp1
        
        for y in range(i+1,n):  # вычитаем из всего i-тую строку
            delta = A[y,i]/A[i,i]
            A[y,i:] = A[y,i:] - A[i,i:]*delta
            B[y] = B[y] - B[i]*delta
    
    X = back_move(A,B)
    out = np.array([X[save[i]] for i in range(n)])
    return out



# мето гауса с частичным выбором главного элемента
def result_nofull(A, B):
    n = A.shape[0] 
    for i in range(n-1):
        index = search_max_line(A[i:,i])
        index += i
        A[[index,i]] = A[[i, index]]
        
        tmp1 = B[index]
        B[index] = B[i]
        B[i] = tmp1
        for y in range(i+1,n):  # вычитаем из всего i-тую строку
            delta = A[y,i]/A[i,i]
            A[y,i:] = A[y,i:] - A[i,i:]*delta
            B[y] = B[y] - B[i]*delta
    out = back_move(A,B)
    return out






