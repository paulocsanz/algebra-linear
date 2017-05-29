from math import log, exp


def TaylorEDO2 (x0, dx0, t0, tf, h, F):
	xold = x0
	dxold = dx0
	told = t0

	while (told <= tf):
		print(told, " - ", xold)
		ddxold = F(xold, dxold, told)
		xold = xold + dxold*h + (ddxold/2)*h**2
		dxold = dxold + ddxold*h 
		told = round(told + h,3)

ddX = lambda x, dx, t: -9.807-1*dx*abs(dx)

TaylorEDO2(0, 0, 0, 1, 0.1, ddX)