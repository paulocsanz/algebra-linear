#!/usr/bin/python3

from math import log, cosh, tanh, sqrt, cos, sin, e
from erros import NaoConverge
from bissecao import raiz as raiz_bissecao
from newton import raiz as raiz_newton
from secante import raiz as raiz_secante
from interpolacao_inversa import raiz as raiz_interpolacao
from eq_n_linear_newton import SolucaoEqNLinearNewton
from eq_n_linear_broyden import SolucaoEqNLinearBroyden
from ajuste_n_linear import AjusteNLinear

print("Questao 1:")
g = 9.806
k = 0.00341
c = sqrt(g * k)
f = lambda x: log(cosh(x * c)) - 50
df = lambda x: g * tanh(x * c)

print("    1) Raiz por bisseçao:\n    ", raiz_bissecao(0, 1000, 0.0001, f))

try:
    print("    2) Raiz por Newton original:\n    ", raiz_newton(1000, 5, f, df, 0.0001))
except ZeroDivisionError as ex:
    print("    2) O resultado da derivada da funçao para x = {} é zero, "
          "portanto ocorre uma divisao por zero durante a resoluçao pelo método de Newton.".format(str(ex)))
except NaoConverge:
    print("    2) Raiz por Newton original nao converge")

try:
    print("    3) Raiz por Newton secante:\n    ", raiz_secante(1000, 5, f, 0.0001))
except NaoConverge:
    print("    3) Raiz por Newton secante nao converge")

try:
    print("    4) Raiz por interpolaçao inversa:\n    ", raiz_interpolacao(f, 0, 10, 20, 1000, 0.0001))
except NaoConverge:
    print("    4) Raiz por interpolacao inversa nao converge")

print("\nQuestao 2:")
f = lambda x: 4 * cos(x) - e**(2*x)
df = lambda x: -2 * (e**(2*x) + 2 * sin(x))

print("    1) Raiz por bisseçao:\n    ", raiz_bissecao(0, 15, 0.0001, f))

try:
    print("    2) Raiz por Newton original:\n    ", raiz_newton(1000, 5, f, df, 0.0001))
except ZeroDivisionError as ex:
    print("    2) O resultado da derivada da funçao para x = {} é zero, "
          "portanto ocorre uma divisao por zero durante a resoluçao pelo método de Newton.".format(str(ex)))
except NaoConverge:
    print("    2) Raiz por Newton nao converge")

try:
    print("    3) Raiz por Newton secante:\n    ", raiz_secante(1000, 10, f, 0.0001))
except NaoConverge:
    print("    3) Raiz por secante nao converge")

try:
    print("    4) Raiz por interpolaçao inversa:\n    ", raiz_interpolacao(f, 0, 5, 10, 1000, 0.0001))
except NaoConverge:
    print("    4) Raiz por interpolacao inversa nao converge")

print("\nQuestao 3:")

F = lambda x: [[16 * x[0]**4 + 16 * x[1]**4 + x[2]**4 - 16],
               [x[0]*x[0] + x[1]*x[1] + x[2]*x[2] - 3],
               [x[0]**3 - x[1] + x[2] - 1]]
J = lambda x: [[64 * x[0]**3, 64 * x[1]**3, 4 * x[2]**3],
               [2*x[0], 2*x[1], 2*x[2]],
               [3 * x[0]*x[0], -1, 1]]
try:
    print("    1) Newton N equaçoes:")
    for v in SolucaoEqNLinearNewton([0.5, 1, 2], 0.0001, 1000, J, F):
        print("        {:.4f}".format(v))
except NaoConverge:
    print("    1) Método por Newton para N equaçoes nao converge")

J = [[64, 64, 4],
    [2, 2, 2],
    [3, -1, 1]] #jacobiana de partida
try:
    print("    2) Método de Broyden:")
    for v in SolucaoEqNLinearBroyden([0.5, 1, 2], J, 0.0001, 1000, F):
        print("        {:.4f}".format(v))
except NaoConverge:
   print("    2) Método de Broyden nao converge")

print("\nQuestao 4:")
F = lambda x: [[2 * x[1]*x[1] + x[0]*x[0] + 6 * x[2]*x[2] - 1],
               [8 * x[1]**3 + 6 * x[1] * x[0]*x[0] + 36 * x[1] * x[0] * x[2] + 108 * x[1] * x[2]*x[2] - theta1],
               [60 * x[1]**4 + 60 * x[1]*x[1] * x[0]*x[0] + 576 * x[1]*x[1] * x[0] * x[2] + 2232 * x[1]*x[1] * x[2]*x[2] + 252 * x[2]*x[2] * x[0]*x[0] + 1296 * x[2]**3 * x[0] + 3348 * x[2]**4 + 24 * x[0]**3 * x[2] + 3 * x[0] - theta2]]

J = lambda x: [[2 * x[0], 4 * x[1], 2 * x[2]],
               [12 * x[0], 24 * x[1]*x[1] + 6 + 36 + 108, 36 + 216 * x[2]],
               [120 * x[0] + 576 + 504 * x[0] + 1296 + 3348 * 3 * x[0]*x[0], 240 * x[1]**3 + 120 * x[1] + 1154 * x[1] + 4464 * x[1], 576 + 4464 * x[2] + 504 * x[2] + 1296 * 3 * x[2]*x[2] + 3348 * 4 * x[2]**3 + 24]]

print("    a)")
theta1, theta2 = 0, 3
try:
    print("    Newton:", SolucaoEqNLinearNewton([0, 0.01, 0.02], 0.00001, 1000, J, F))
except NaoConverge:
    print("    Método de Newton nao converge")

print("    b)")
theta1, theta2 = 0.75, 6.5
try:
    print("    Newton:", SolucaoEqNLinearNewton([0, 0.01, 0.02], 0.00001, 1000, J, F))
except NaoConverge:
    print("    Método de Newton nao converge")

print("    c)")
theta1, theta2 = 0, 11.667
try:
    print("    Newton:", SolucaoEqNLinearNewton([0, 0.01, 0.02], 0.00001, 1000, J, F))
except NaoConverge:
    print("    Método de Newton nao converge")

print("\nQuestao 5:")
F = lambda x,b,y: [b[0][0] + b[1][0] * x**b[2][0] - y]
J = lambda x,b: [1, x**b[2][0], b[1][0] * x**b[2][0] * log(x)]
try:
    resp5 = AjusteNLinear ([1,2,3], [1,2,9], [[1], [1], [2]], 0.0001, 100, J, F)
    print("Ajuste Nao Linear:\n","\nb1 = ", resp5[0][0],"\nb2 = ", resp5[1][0],"\nb3 = ", resp5[2][0])
except NaoConverge:
    print("Ajuste nao converge")
