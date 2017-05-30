import matplotlib.pyplot as plt
from threading import Thread
from euler import EulerEDO
from runge_kutta_2a import RungeKutta2aEDO
from runge_kutta_4a import RungeKutta4aEDO
from runge_kutta_nystrom_edo2 import RungeKuttaNystromEDO2
from serie_taylor_edo2 import TaylorEDO2
from math import e, pi, log, sqrt, cos, sin

def plot(array, title, color='blue'):
    fig = plt.figure(figsize=(8, 6), dpi=80)
    ax = plt.subplot(111)
    plt.plot(range(len(array)),
             array,
             color=color,
             linewidth=1.0,
             linestyle="-")
    ax.set_title(title)
    plt.grid(True)
    plt.ylabel('x(t)')
    plt.xlabel('s')

    fig.show()

print("Exercício 1")
f = lambda x, t: -2*t*(x**2)
print("    Euler")
for told, xold in EulerEDO(1, 0, 2, 0.005, f):
    print("        {:.3f} - {:.9f}".format(told, xold))

print("\n    RK2")

for told, xold in RungeKutta2aEDO(1,0,2,0.05,f):
    print("        {:.1f} - {:.9f}".format(told, xold))

print("\n    RK4")
for told, xold in RungeKutta4aEDO(1,0,2,0.1,f):
    print("        {:.1f} - {:.9f}".format(told, xold))

print("\n    Referencia")
i=0
while(i<=2):
    ref = 1/(1+i**2)
    print("        {:.1f} - {:.9f}".format(i, ref))
    i=round(0.1+i,3)

c = 0.2
k = 1
w = 0.5
f = lambda x, dx, t: 2*sin(w*t) + sin(2*w*t) + cos(3*w*t) - c*dx - k*x
runge_kutta = RungeKuttaNystromEDO2 (0, 0, 0, 100, 0.1, f)
taylor = TaylorEDO2 (0, 0, 0, 100, 0.1, f)

plot(runge_kutta, "Exercício 2: Método Runge-Kutta")
plot(taylor, "Exercício 2: Método de Taylor", color='red')

print("\nExercício 2")
print("    index    Runge-Kutta    Taylor")
for i in range(len(runge_kutta)):
    print("    {:3}    -   {:+.4f}   - {:+.4f}".format(
          i,
          runge_kutta[i],
          taylor[i]))

f = lambda x, dx, t: -9.807-1*dx*abs(dx)
runge_kutta = RungeKuttaNystromEDO2(0, 0, 0, 20, 0.1, f)
taylor = TaylorEDO2(0, 0, 0, 20, 0.1, f)

plot(runge_kutta, "Exercício 3: Método Runge-Kutta")
plot(taylor, "Exercício 3: Método de Taylor", color='red')

print("\nExercício 3")
print("    index    Runge-Kutta    Taylor")
for i in range(len(runge_kutta)):
    print("     {:2}   -   {}{:+.4f}   - {}{:+.4f}".format(
          i,
          " " if abs(runge_kutta[i]) < 10 else "",
          runge_kutta[i],
          " " if abs(taylor[i]) < 10 else "",
          taylor[i]))
# Ultima coisa no script (bloqueia até os gráficos fecharem)
try:
    plt.show()
except KeyboardInterrupt:
    pass
