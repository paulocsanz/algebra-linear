from erros import NaoConverge
from numpy import matrix
from numpy.linalg import inv
from numpy.linalg import norm

def SolucaoEqNLinearNewton(xin, tol, niter, J, F):
    xold = xin
    tolerancia = 1

    while (tolerancia > tol and niter != -1):
        f = matrix(F(xold))
        if f.size == 1:
            f = f.transpose()
        j = J(xold)
        jinv = inv(j)
        deltax = -1 * jinv * f
        deltax = deltax.transpose()
        xnew = deltax + xold 
        tolerancia = norm(deltax) / norm(xnew)
        niter -= 1
        xold = list(xnew.flat)

    if niter == -1:
        raise NaoConverge
    return xold

if __name__ == "__main__":
    F = lambda x: [x[0] + 2 * x[1] - 2, x[0]*x[0] + 4 * x[1]*x[1] - 4]
    J = lambda x: [[1, 2], [2 * x[0], 8 * x[1]]]
    try:
        print(SolucaoEqNLinearNewton([2,3], 0.0001, 100, J, F))
    except NaoConverge:
        print("Convergence not reached")
