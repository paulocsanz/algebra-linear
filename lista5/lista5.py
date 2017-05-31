from integracao_polinomial import integracao_polinomial
from quadratura_gauss import QuadraturaGauss as quadratura_gauss
from math import e, pi, sqrt

print("Questao 2:")
f = lambda x: 1/sqrt(2 * pi) * e ** -(x**2/2)
print("    I1)")
print("        Integraçao polinomial: {:.4f}".format(integracao_polinomial(f, 0, 1, 10)))
print("        Quadratura de Gauss:   {:.4f}".format(quadratura_gauss(0, 1, 10, f)))

print("    I2)")
print("        Integraçao polinomial: {:.4f}".format(integracao_polinomial(f, 0, 5, 10)))
print("        Quadratura de Gauss:   {:.4f}".format(quadratura_gauss(0, 5, 10, f)))

print("\nQuestao 3:")

wn = 1
E = 0.05
sn = lambda x: 2
rao = lambda x: 1/sqrt((1 - (x/wn)**2)**2 + (2 * E * x/wn)**2)
f = lambda x: rao(x)**2 * sn(x)
g = lambda x: f(x) * x**2
#f = lambda x: 2 / (0.01*x**2 + (1-x**2)**2) MESMA COISA SÓ Q SIMPLIFICADO
print("    Integraçao polinomial:")
print("        m0: {:.4f}".format(integracao_polinomial(f, 0, 10, 10)))
print("        m2: {:.4f}".format(integracao_polinomial(g, 0, 10, 10)))
print("    Quadratura de Gauss:")
print("        m0: {:.4f}".format(quadratura_gauss(0, 10, 10, f)))
print("        m2: {:.4f}".format(quadratura_gauss(0, 10, 10, g)))

print("\nQuestao 4:") 
hs = 3
tz = 5
sn = lambda x: 4*pi**3*hs**2/(x**5 * tz**4)*e**(-16*pi**3/(x**4* tz**4))

print("    Integraçao polinomial:")
print("        m0: {:.4f}".format(integracao_polinomial(f, 0.00001, 10, 10)))
print("        m2: {:.4f}".format(integracao_polinomial(g, 0.00001, 10, 10)))
print("    Quadratura de Gauss:")
print("        m0: {:.4f}".format(quadratura_gauss(0.00001, 10, 10, f)))
print("        m2: {:.4f}".format(quadratura_gauss(0.00001, 10, 10, g)))

print("\nQuestao 5:")
f = lambda x: 2 + 2 * x - x**2 + 3 * x**3
print("    Integraçao polinomial: {:.4f}".format(integracao_polinomial(f, 0, 4, 3)))
print("    Quadratura de Gauss:   {:.4f}".format(quadratura_gauss(0, 4, 2, f)))

print("\nQuestao 6:")
f = lambda x: 1/(1 + x*x)
print("    a) Regra do ponto médio:")
print("        Integraçao polinomial: {:.4f}".format(integracao_polinomial(f, 0, 3, 2)))
print("        Quadratura de Gauss:   {:.4f}".format(quadratura_gauss(0, 3, 2, f)))

print("    b) Regra do trapézio:")
print("        Integraçao polinomial: {:.4f}".format(integracao_polinomial(f, 0, 3, 4)))
print("        Quadratura de Gauss:   {:.4f}".format(quadratura_gauss(0, 3, 4, f)))

print("    c) Regra de Simpson:")
print("        Integraçao polinomial: {:.4f}".format(integracao_polinomial(f, 0, 3, 3)))
print("        Quadratura de Gauss:   {:.4f}".format(quadratura_gauss(0, 3, 3, f)))
