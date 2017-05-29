from erros import NaoConverge
from numpy import matrix
from numpy.linalg import inv
from numpy.linalg import norm

def SolucaoEqNLinearBroyden(xin, bi, tol, niter, F):
    xold = xin
    bold = matrix(bi) 
    tolerancia = 1

    while (tolerancia > tol and niter != -1):
            f = matrix(F(xold))
            if f.size == 1:
                f = f.transpose()
            j = bold
            jinv = inv(j)
            deltax = -1 * jinv * f
            deltax = deltax.transpose() #usado para realizar a soma com Xold
            xnew = deltax + xold
            deltax = deltax.transpose() #voltar ao normal

            xnew = list(xnew.flat)
            y = matrix(F(xnew)) - matrix(F(xold))

            bnew = bold + ((y - bold*deltax)*deltax.transpose()) / (deltax.transpose()*deltax)

            tolerancia = norm(deltax) / norm(xnew)
            niter -= 1
            xold = xnew
            bold = bnew
    if niter == -1:
        raise NaoConverge
    return xold

if __name__ == "__main__":
    F = lambda x: [[x[0] + 2 * x[1] - 2], [x[0]*x[0] + 4 * x[1]*x[1] - 4]]
    try:
        print(SolucaoEqNLinearBroyden([2,3], [[1,2],[4,24]], 0.0001, 100, F))
    except NaoConverge:
        print("Convergence not reached")
