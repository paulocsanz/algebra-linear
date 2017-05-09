class NaoEncontrado(Exception):
    pass

def raiz(n, x0, func, dfunc, tol):
    x = x0
    for i in range(n):
        x0 = x
        x = x0 - func(x0)/dfunc(x0)
        if abs(x - x0) <= tol:
            return x
    raise NaoEncontrado

from math import cos, sin
f = lambda x: x**2 - 4*cos(x)
df = lambda x: 2*x + 4* sin(x)
print("{:.3f}".format(raiz(10, 10, f, df, 0.0005)))
