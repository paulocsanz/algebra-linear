#!/usr/bin/env python3

from erros import NaoConverge

def raiz(func, x1, x2, x3, n_iteracoes, tol):
    x = [0, x1, x2, x3]
    for i in range(n_iteracoes):
        y = [func(v) for v in x]
        x = ([x[0]] +
             [(x[1] * y[2] * y[3] / float((y[1] - y[2]) * (y[1] - y[3]))   +
               x[2] * y[1] * y[3] / float((y[2] - y[1]) * (y[2] - y[3]))   +
               x[3] * y[1] * y[2] / float((y[3] - y[1]) * (y[3] - y[2])))] +
             x[1:])
        if (abs(x[1] - x[0]) < tol):
            return x[1]

        x[0] = x[1]
        x.pop(1)

        max_y = y[0]
        index = 3
        for i, v in enumerate(y[1:]):
            if v > max_y:
                v = max_y
                index = i+1
        x[index] = x[0]

    raise NaoConverge

if __name__ == "__main__":
    from math import cos
    f = lambda x: x**2 - 4 * cos(x)
    print(raiz(f, 3, 5, 10, 100, 5/10000))
