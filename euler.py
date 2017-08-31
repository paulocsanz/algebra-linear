#!/usr/bin/env python3

from math import log, exp


def EulerEDO (x0, t0, tf, h, dX):
    xold = x0
    told = t0

    ret = []
    while (told <= tf):
        ret += [(told, xold)]
        k1 = dX(xold, told)
        xold = xold + k1 * h
        told = round(told + h,3)
    return ret

# dX = lambda x, t: t + x
# EulerEDO(0, 0, 1, 0.01, dX)
