class NaoConverge(Exception):
    pass

def raiz_interpolacao_inversa(func, x1, x2, x3, n_iteracoes, tol):
    x = [10E+36, x1, x2, x3]
    for i in range(n_iteracoes):
        y = tuple(func(v) for v in x)
        x += [(y[2] * y[3] * x[1]) / ((y[1] - y[2]) * (y[1] - y[3])) +
              (y[1] * y[3] * x[2]) / ((y[2] - y[1]) * (y[2] - y[3])) +
              (y[1] * y[2] * x[3]) / ((y[3] - y[1]) * (y[3] - y[2]))]
        if (abs(x[4] - x[3]) < tol):
            return x[4]
        else:
            x.pop(3)
            x.sort()
    raise NaoConverge

from math import cos
f = lambda x: x**2 - 4 * cos(x)
print(raiz_interpolacao_inversa(f, 3, 5, 10, 100, 5/10000))
