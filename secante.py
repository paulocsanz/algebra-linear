#!/usr/bin/python3

from erros import NaoConverge

def raiz(n, x0, func, tol):
    delta = 0.001
    valores = [x0, x0 + delta]
    y0 = func(x0)
    for i in range(1, n+1):
        y = func(valores[i])
        valores += [valores[i] - y * (valores[i] - valores[i-1])/(y - y0)]
        if abs(valores[i+1] - valores[i]) <= tol:
            return valores[i+1]
        else:
            y0 = y
    raise NaoConverge

if __name__ == "__main__":
    from math import cos, sin
    f = lambda x: x**2 - 4*cos(x)
    print("{:.3f}".format(raiz(10, 10, f, 0.0005)))
