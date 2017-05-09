def raiz(inicio, fim, tol, func):
    crescente = 1 if func(fim) > func(inicio) else -1
    while abs(fim - inicio) > tol:
        x = (inicio + fim)/2
        y = func(x)
        if y == 0: 
            return x
        elif crescente * y > 0:
            fim = x
        else:
            inicio = x
    return x

from math import cos
f = lambda x: x**2 - 4*cos(x)
print("{:.5f}".format(raiz(0, 10, 0.0001, f)))
