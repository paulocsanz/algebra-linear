#!/usr/bin/env python3

from math import log, exp

def RungeKutta4aEDO (x0, t0, tf, h, dX):
    xold = x0
    told = t0

    ret = []
    while (told <= tf):
        ret += [(told, xold)]
        k1 = dX(xold, told)
        k2 = dX(xold + h/2*k1, told+h/2)
        k3 = dX(xold + h/2*k2, told+h/2)
        k4 = dX(xold + h*k3, told+h)
        xold = xold + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        told = round(told + h,3)
    return ret

if __name__ == "__main__":
    dX = lambda x, t: t + x
    RungeKutta4aEDO(0, 0, 1, 0.1, dX)
