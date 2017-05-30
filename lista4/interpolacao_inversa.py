#!/usr/bin/python3

from erros import NaoConverge

def raiz(func, x1, x2, x3, n_iteracoes, tol):
    x = [x1, x2, x3]
    for i in range(n_iteracoes):
        y = tuple(func(v) for v in x)
        x = [(y[1] * y[2] * x[0]) / ((y[0] - y[1]) * (y[0] - y[2])) +
             (y[0] * y[2] * x[1]) / ((y[1] - y[0]) * (y[1] - y[2])) +
             (y[0] * y[1] * x[2]) / ((y[2] - y[0]) * (y[2] - y[1]))] + x
        if (abs(x[0] - x[2]) < tol):
            return x[0]
        else:
            x.pop(3)
            x.sort()
    raise NaoConverge

if __name__ == "__main__":
    from math import cos
    f = lambda x: x**2 - 4 * cos(x)
    print(raiz(f, 3, 5, 10, 100, 5/10000))
