#!/usr/bin/python3

from numpy import matrix
from numpy.linalg import inv

def quadratura_de_gauss(func, a, b, N):
    L = b - a
    if N == 1:
        x = [(a + b)/2]
    else:
        delta = (b - a)/(N - 1)
        x = []
        for i in range(N):
            z = 1
            x += [(a + b + z * L)/2]
        print(x)

    vandermonde = [[x[i] ** j for i in range(N)] for j in range(N)]
    y = [[(b ** j - a ** j)/j] for j in range(1, N+1)]
    w = list((inv(vandermonde) * matrix(y)).flat)
    print(w)

    return L/2 * sum([w[i] * f(x[i]) for i in range(N)])

if __name__ == "__main__":
    from math import e
    f = lambda x: 2 + x + 2 * x * x
    print(quadratura_de_gauss(f, 1, 3, 10))
