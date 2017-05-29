from integracao_polinomial import integracao_polinomial
from math import e, pi, sqrt

print("Questão 2:")
f = lambda x: 1/sqrt(2 * pi) * e ** -(x**2/2)
print("Integração polinomial:", integracao_polinomial(f, 0, 1, 10))

print("")

print("Questão 3:")

wn = 1
E = 0.05
sn = lambda x: 2
rao = lambda x: 1/sqrt((1 - (x/wn)**2)**2 + (2 * E * x/wn)**2)
f = lambda x: rao(x)**2 * sn(x)
print("Integração polinomial:")
print("m0:", integracao_polinomial(f, 0, 10, 10))
g = lambda x: f(x) * x**2
print("m2:", integracao_polinomial(g, 0, 10, 10))

print("Questão 4")
hs = 3
tz = 5
sn = lambda x: 4*pi**3*hs**2/(x**5 * tz**4)*e**(-16*pi**3/(x**4* tz**4))
print("Integração polinomial:")
# Com essa função sn ta dando divisão por 0, pq a integral começa em 0 e a função divide por x, ai crasha, comofas?
#print("m0:", integracao_polinomial(f, 0, 10, 10))
#print("m2:", integracao_polinomial(g, 0, 10, 10))

print("Questão 5")
f = lambda x: 2 + 2 * x - x**2 + 3 * x**3
esperado = int(integracao_polinomial(f, 0, 4, 10) * 10000)/10000
menor = 10
for p in range (9, 0, -1):
    obtido = int(integracao_polinomial(f, 0, 4, p) * 10000)/10000
    if obtido != esperado:
        menor = p + 1
        break
print("Integração polinomial com {} pontos de integração: {}".format(
      menor,
      esperado))
