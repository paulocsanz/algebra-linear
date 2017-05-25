#!/usr/bin/python3

from numpy import matrix
from numpy.linalg import inv

def integracao_polinomial(func, a, b, N):
    if N == 1:
        x = [(a + b)/2]
    else:
        delta = (b - a)/(N - 1)
        x = [a + i * delta for i in range(N)]

    vandermonde = [[x[i] ** j for i in range(N)] for j in range(N)]
    y = [[(b ** j - a ** j)/j] for j in range(1, N+1)]
    w = list((inv(vandermonde) * matrix(y)).flat)
    return sum([w[i] * f(x[i]) for i in range(N)])

if __name__ == "__main__":
    from math import e
    f = lambda x: e ** (-x ** 2)
    print(integracao_polinomial(f, 0, 1, 10))
