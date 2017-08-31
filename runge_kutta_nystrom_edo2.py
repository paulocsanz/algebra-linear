#!/usr/bin/env python3

from math import log, exp

def RungeKuttaNystromEDO2 (x0, dx0, t0, tf, h, F):
	xold = x0
	dxold = dx0
	told = float(t0)
	lista = []

	while (told <= tf):
		# print(told, " - ", xold)
		if(told).is_integer():
			lista += [xold]
		k1 = 1/2 * h * F(xold, dxold, told)
		q = 1/2 * h * (dxold + 1/2*k1)
		k2 = 1/2 * h * F(xold+q, dxold+k1, told + h/2)
		k3 = 1/2 * h * F(xold+q, dxold+k2, told + h/2)
		l = h * (dxold + k3)
		k4 = 1/2 * h * F(xold+l,dxold+2*k3,told+h)
		xold = xold + h*(dxold+1/3*(k1+k2+k3))
		dxold = dxold + 1/3*(k1 + 2*k2 + 2*k3 + k4)
		told = round(told + h,3)
	return lista

if __name__ == "__main__":
    ddX = lambda x, dx, t: -9.807-1*dx*abs(dx)
    RungeKuttaNystromEDO2(0, 0, 0, 1, 0.1, ddX)
