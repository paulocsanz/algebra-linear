from euler import EulerEDO
from runge_kutta_2a import RungeKutta2aEDO
from runge_kutta_4a import RungeKutta4aEDO
from math import e, pi, log, sqrt

print("Exercício 1")
f = lambda x, t: -2*t*(x**2)
print("Euler")
EulerEDO(1,0,2,0.1,f)

print("RK2")
RungeKutta2aEDO(1,0,2,0.1,f)

print("RK4")
RungeKutta4aEDO(1,0,2,0.1,f)

print("Referencia")
for i in range (0,2,0.1):
	ref = 1/(1+i**2)
	print(ref)
