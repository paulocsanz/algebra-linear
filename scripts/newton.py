#!/usr/bin/env python3

from erros import NaoConverge

def raiz(n, x0, func, dfunc, tol):
    x = x0
    for i in range(n):
        x0 = x
        y = func(x0)
        dy = dfunc(x0)

        if dy == 0:
            raise ZeroDivisionError(x0)
        x = x0 - y/dy

        if abs(x - x0) <= tol:
            return x
    raise NaoConverge

if __name__ == "__main__":
    from math import cos, sin
    f = lambda x: x**2 - 4*cos(x)
    df = lambda x: 2*x + 4* sin(x)
    print("{:.3f}".format(raiz(10, 10, f, df, 0.0005)))
