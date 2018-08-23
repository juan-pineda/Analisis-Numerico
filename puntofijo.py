import numpy as np
from pylab import *

def polinomio(x):
	y = x**2 - x -2
	return y

x = np.arange(0,5,0.3)
plot(x,polinomio(x),"-sr",markersize=2)
savefig("polinomio.png")
# clf es clear figure, para liberar espacio en memoria
clf()

def fixed_point_iteration(f,x0,tol):
    n_iter = 0
    tol_n = 100
    x_old = x0
    while ((tol_n > tol) & (n_iter < 1e5)):
        x_new = f(x_old)
        tol_n = x_new - x_old
        n_iter = n_iter+1
        x_old = x_new
        print(x_old)
    if tol_n < tol:
        print("Bravoooo")
        print("El algoritmo convergio!!!!")
        print("el valor de x es ", x_old )
        return x_old
    else:
        print("alcanzo numero de iteraciones limite")
        return None


def g(x):                           
    return np.sqrt(x+2)


x_fijo = fixed_point_iteration(g,1,1e-7)

