from numpy import matrix
from numpy.linalg import inv
from numpy.linalg import norm


F = lambda x: [x[0] + 2 * x[1] - 2, x[0]*x[0] + 4 * x[1]*x[1] - 4]
J = lambda x: [[1, 2], [2 * x[0], 8 * x[1]]]

def SolucaoEqNLinearNewton (xin, tol, niter, J, F):
	xold = xin
	tolerancia = 1

	while (tolerancia > tol and niter != -1):
		print(xold)
		f = matrix(F(xold))
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
		print("Convergence not reached")
	else:
		print(xold)


SolucaoEqNLinearNewton([2,3], 0.0001, 100, J, F)