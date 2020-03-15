# %matplotlib inline
import numpy as np                  #для работы с массивами - их по умолчанию в Python нет
import scipy
from scipy import linalg
#1
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, -1, 12]], float)     #создание матрицы
print(a.shape)                                                          #размерность матрицы
b = np.array([[1, 2, 3]], float)                                        #создание вектора

b = a * 2                                       #умножение на число - умножается каждый элемент
print(b)

c = a + 1                                       #добавление числа - добавляется к каждоме элементу
print(c)
d = c + b                                       #сложение матриц - складываеются матрица при каждом ее члене
d = np.add(b, c)			                    #тоже самое через функцию в NP

d = b - c 			                            #вычитание матриц - вычитание матрица при каждом ее члене
d = np.subtract(b, c)                           #тоже самое через функцию в NP
print(d)

f = d.transpose()                               #транспонирование
d.T
print(f)

g = np.dot(f, d)                                #умножение матриц
print(g)

e = np.identity(3)                              #создание единичной матрицы порядка 3
print(e)

p = np.linalg.inv(g)                            #создание обратной матиццы
print(p)

aa = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.linalg.det(aa)                                #определитель
np.linalg.matrix_rank(b, 0.0001)                 #ранк матрицы

#2 СЛАУ
print('##########')
A = np.array([[3, 2], [3, -4]])
B = np.array([4, 1])
np.linalg.solve(A, B)                           # решение СЛАУ

P, L, U =  linalg.lu(A)                         # LU разложение СЛА
print(P, L, U)

A = np.array([[1, 2, -1], [3, -4, 0], [8,-5, 2], [2,0, -5], [11, 4, -7]])
B = np.array([1, 7, 12, 7, 15])
X, q, rank, p = np.linalg.lstsq(A, B)           # решение по метода наименьшиъ квадраов

#!!! Не проверенно
L =  scipy.linalg.choletsky(A)                  #разложение Хлецкого - для симметричных матриц
Q, R =  np.linalg.qr(A)                         #QR разложение
np.concatenate(A, B)                            # склеивание матриц
