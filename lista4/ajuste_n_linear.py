from erros import NaoConverge
from numpy import matrix
from numpy.linalg import inv
from numpy.linalg import norm

def AjusteNLinear (xin, yin, bi, tol, niter, J, F):
    bold = bi 
    tolerancia = 1

    while (tolerancia > tol and niter != -1):
        j = J(xin[0],bold), J(xin[1],bold), J(xin[2],bold)
        j = matrix(j)
        f = F(xin[0],bold,yin[0]), F(xin[1],bold,yin[1]), F(xin[2],bold,yin[2])
        f = matrix(f)

        deltab = - inv(j.transpose()*j) * j.transpose() * f
        bold = bold + deltab 
        tolerancia = norm(deltab) / norm(bold)
        bold = list(bold.flat)
        bold = [[bold[0]],[bold[1]]]

    if niter == -1:
        raise NaoConverge

    return bold

if __name__ == "__main__":
    from math import log, exp
    J = lambda x,b: [x**b[0][0] * log(x)/b[1][0] * exp((x**b[0][0])/b[1][0]) , -x**b[0][0] * x**b[0][0]/b[1][0]**2 * exp((x**b[0][0])/b[1][0])]
    F = lambda x,b,y: [exp((x**b[0][0])/b[1][0])-y]

    try:
        print(AjusteNLinear([1,2,3], [1.995,1.410,1.260] ,[[0],[1]], 0.0001, 100, J, F))
    except NaoConverge:
        print("Não converge")
