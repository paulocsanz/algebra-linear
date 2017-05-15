#!/usr/bin/python3

from math import log, cosh, tanh, sqrt
from erros import NaoConverge
from bissecao import raiz as raiz_bissecao
from newton import raiz as raiz_newton
from secante import raiz as raiz_secante
from interpolacao_inversa import raiz as raiz_interpolacao

g = 9.806
k = 0.00341
c = sqrt(g * k)
f = lambda x: log(cosh(x * c)) - 50
df = lambda x: g * tanh(x * c)

print("1) Raiz por bisseção:\n", raiz_bissecao(0, 1000, 0.0001, f))

try:
    print("2) Raiz por Newton original:\n", raiz_newton(1000, 5, f, df, 0.0001))
except ZeroDivisionError as ex:
    print("2) O resultado da derivada da função para x = {} é zero, "
          "portanto ocorre uma divisão por zero.".format(str(ex)))
except NaoConverge:
    print("2) Raiz por Newton original não converge")

try:
    print("3) Raiz por Newton secante:\n", raiz_secante(1000, 5, f, 0.0001))
except NaoConverge:
    print("3) Raiz por Newton secante não converge")

try:
    print("4) Raiz por interpolação inversa:\n", raiz_interpolacao(f, 0, 1, 2, 1000, 0.0001))
except NaoConverge:
    print("4) Raiz por interpolacao inversa não converge")
