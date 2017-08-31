#!/usr/bin/env python3

from numpy import dot

weights = [[2],
           [1, 1],
           [0.8888888, 0.5555556, 0.5555556],
           [0.6521451, 0.6521451, 0.3478548, 0.3478548],
           [0.5688889, 0.4786287, 0.4786287, 0.2369269, 0.2369269],
           [0.3607616, 0.3607616, 0.4679139, 0.4679139, 0.1713245, 0.1713245],
           [0.4179592, 0.3818300, 0.3818300, 0.2797054, 0.2797054, 0.1294850, 0.1294850],
           [0.3626838, 0.3626838, 0.3137066, 0.3137066, 0.2223810, 0.2223810, 0.1012285, 0.1012285],
           [0.3302393, 0.1806482, 0.1806482, 0.0812744, 0.0812744, 0.3123471, 0.3123471, 0.2606107, 0.2606107],
           [0.2955242, 0.2955242, 0.2692667, 0.2692667, 0.2190864, 0.2190864, 0.1494513, 0.1494513, 0.0666713, 0.0666713]]

zi = [[0],
      [-0.5773502691896257, 0.5773502691896257],
      [0, -0.7745966692414834, 0.7745966692414834],
      [-0.3399810435848563, 0.3399810435848563, -0.8611363115940526, 0.8611363115940526],
      [0, -0.5384693101056831, 0.5384693101056831, -0.9061798459386640, 0.9061798459386640],
      [-0.6612093864662645, 0.6612093864662645, -0.2386191860831969, 0.2386191860831969, -0.9324695142031521, 0.9324695142031521],
      [0, -0.4058451513773972, 0.4058451513773972, -0.7415311855993945, 0.7415311855993945, -0.9491079123427585, 0.9491079123427585],
      [-0.1834346424956498, 0.1834346424956498, -0.5255324099163290, 0.5255324099163290, -0.7966664774136267, 0.7966664774136267, -0.9602898564975363, 0.9602898564975363],
      [0, -0.8360311073266358, 0.8360311073266358, -0.9681602395076261, 0.9681602395076261, -0.3242534234038089, 0.3242534234038089, -0.6133714327005904, 0.6133714327005904],
      [-0.1488743389816312, 0.1488743389816312, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]]

def QuadraturaGauss (a, b, n, F):
    X = lambda z, a, b, L: 1/2 * (a + b + z*L)
    L = b - a

    xi = [X(zi[n-1][i], a, b, L) for i in range(0,n)]   # gera os pontos não normalizados, a partir de zi
    fi = [F(xi[i]) for i in range(0, n)]                # aplica os pontos na função de entrada

    return L/2 * (dot(fi,weights[n-1])) 

if __name__ == "__main__":
    from math import e
    F = lambda x: e ** (-x ** 2)
    print(QuadraturaGauss(0, 1, 10, F))