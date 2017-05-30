from euler import EulerEDO
from runge_kutta_2a import RungeKutta2aEDO
from runge_kutta_4a import RungeKutta4aEDO
from runge_kutta_nystrom_edo2 import RungeKuttaNystromEDO2
from serie_taylor_edo2 import TaylorEDO2
from math import e, pi, log, sqrt, cos, sin

print("Exercício 1")
f = lambda x, t: -2*t*(x**2)
print("Euler")
EulerEDO(1,0,2,0.005,f)

print("\nRK2")
RungeKutta2aEDO(1,0,2,0.05,f)

print("\nRK4")
RungeKutta4aEDO(1,0,2,0.1,f)

print("\nReferencia")
i=0
while(i<=2):
	ref = 1/(1+i**2)
	print(i," - ",ref)
	i=round(0.1+i,3)



print("\n\nExercício 2")
c = 0.2
k = 1
w = 0.5
f = lambda x, dx, t: 2*sin(w*t) + sin(2*w*t) + cos(3*w*t) - c*dx - k*x
resRKN = RungeKuttaNystromEDO2 (0, 0, 0, 100, 0.1, f)
resT = TaylorEDO2 (0, 0, 0, 100, 0.1, f)

for i in range(0,10): #TA AQUI SO PA EU TESTA AS PARADA MAL PODE COMENTA
	print(resRKN[i], " - ", resT[i])




print("\n\nExercício 3")

f = lambda x, dx, t: -9.807-1*dx*abs(dx)
resRKN2 = RungeKuttaNystromEDO2(0, 0, 0, 20, 0.1, f)
resT2 = TaylorEDO2(0, 0, 0, 20, 0.1, f)

for i in range(0,10): #TA AQUI SO PA EU TESTA AS PARADA MAL PODE COMENTA
	print(resRKN2[i], " - ", resT2[i])