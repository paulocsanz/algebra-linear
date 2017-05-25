from integracao_polinomial import integracao_polinomial
from math import e, pi

f = lambda x: 1/(2*pi) * exp(-1/2 * x**2)
print(integracao_polinomial(f, 0, 1, 10))
