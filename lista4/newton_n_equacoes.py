#!/usr/bin/python3

from math import sqrt
from numpy import matrix
from numpy.linalg import inv
from erros import NaoConverge

def multiplicar_escalar(A, escalar):
    C = [[i for i in A] for j in A[0]]
    for i, linha in enumerate(A):
        for j, x in enumerate(linha):
            C[i][j] = A[i][j] * escalar
    return C

def solucao_sistema_equacoes_newton(x0, n_iteracoes, J, F, tol):
    mod = lambda x: sqrt(sum(map(lambda i: i*i, x)))
    x = x0
    for i in range(n_iteracoes):
        x0 = x
        inv_j = inv(J(x0))
        f = matrix(F(x0))
        if type(f[0]) != list:
            f = f.transpose()
        delta_x = -1 * inv_j * f

        if type(x0[0]) != list:
            m0 = matrix([[n] for n in x0])
        else:
            m0 = matrix(x0)

        x = (m0 + delta_x).tolist()
        delta_x = delta_x.transpose().tolist()[0]

        if m0.tolist() != x0:
            x = [i[0] for i in x] 
        if (mod(delta_x)/mod(x) <= tol):
            return x
    raise NaoConverge

F = lambda x: [x[0] + 2 * x[1] - 2, x[0]*x[0] + 4 * x[1]*x[1] - 4]
J = lambda x: [[1, 2], [2 * x[0], 8 * x[1]]]
print(solucao_sistema_equacoes_newton([2, 3], 100, J, F, 1/1000))
