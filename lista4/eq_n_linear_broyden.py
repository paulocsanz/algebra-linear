from numpy import matrix
from numpy.linalg import inv
from numpy.linalg import norm


F = lambda x: [[x[0] + 2 * x[1] - 2], [x[0]*x[0] + 4 * x[1]*x[1] - 4]]

def SolucaoEqNLinearBroyden (xin, bi, tol, niter, F):
	xold = xin
	bold = matrix(bi) 
	tolerancia = 1

	while (tolerancia > tol and niter != -1):
		f = matrix(F(xold))
		#f = f.transpose()
		j = bold
		jinv = inv(j)
		deltax = -1 * jinv * f
		deltax = deltax.transpose() #usado para realizar a soma com Xold
		xnew = deltax + xold
		deltax = deltax.transpose() #voltar ao normal

		xnew = list(xnew.flat)
		y = matrix(F(xnew)) - matrix(F(xold))

		# print(y)
		# print(deltax)
		# print(deltax.transpose())
		# print(bold)
		bnew = bold + ((y - bold*deltax)*deltax.transpose()) / (deltax.transpose()*deltax)

		tolerancia = norm(deltax) / norm(xnew)
		niter -= 1
		xold = xnew
		bold = bnew
		print(xold)
	if niter == -1:
		print("Convergence not reached")
	else:
		print("Fim")
		print(xold)


SolucaoEqNLinearBroyden([2,3], [[1,2],[4,24]], 0.0001, 100, F)