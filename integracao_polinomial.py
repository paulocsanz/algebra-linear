#!/usr/bin/python3

from numpy import matrix
from numpy.linalg import inv
from erros import MuitosPontosDeIntegracao

def integracao_polinomial(func, a, b, N):
    L = b - a
    w = [[L],
         [L/2, L/2],
         [L/6, 2*L/3, L/6],
         [L/8, 3*L/8, 3*L/8, L/8],
         [7*L/90, 16*L/45, 2*L/15, 16*L/45, 7*L/90]]
    if len(w) < N:
        raise MuitosPontosDeIntegracao("Máximo = {}".format(len(w)))

    if N == 1:
        x = [(a + b)/2]
    else:
        delta = (b - a)/(N - 1)
        x = [a + i * delta for i in range(N)]
    return sum([w[N-1][i] * f(x[i]) for i in range(N)])

if __name__ == "__main__":
    from math import e
    f = lambda x: e ** (-x ** 2)
    print(integracao_polinomial(f, 0, 1, 5))
