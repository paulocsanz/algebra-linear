#!/usr/bin/python3

from math import cos, sin, e
from erros import NaoConverge
from bissecao import raiz as raiz_bissecao
from newton import raiz as raiz_newton
from secante import raiz as raiz_secante
from interpolacao_inversa import raiz as raiz_interpolacao

f = lambda x: 4 * cos(x) - e**(2*x)
df = lambda x: -2 * (e**(2*x) + 2 * sin(x))

print("1) Raiz por bisseção:\n", raiz_bissecao(0, 15, 0.0001, f))

try:
    print("2) Raiz por Newton original:\n", raiz_newton(1000, 5, f, df, 0.0001))
except ZeroDivisionError as ex:
    print("2) O resultado da derivada da função para x = {} é zero, "
          "portanto ocorre uma divisão por zero.".format(str(ex)))
except NaoConverge:
    print("2) Raiz por Newton não converge")

try:
    print("3) Raiz por Newton secante:\n", raiz_secante(1000, 10, f, 0.0001))
except NaoConverge:
    print("3) Raiz por secante não converge")

try:
    print("4) Raiz por interpolação inversa:\n", raiz_interpolacao(f, 5, 10, 15, 1000, 0.0001))
except NaoConverge:
    print("4) Raiz por interpolacao inversa não converge")
