import numpy as np
import matplotlib.pyplot as plt
from math import *
import sympy as sy
from scipy.linalg import eigh_tridiagonal
from sympy import var
from sympy import sympify

    # Setting up the Grid
n = int(input("Enter n :"))
dy = 1/n
y = np.linspace(0,1,n+1)

    #Potential
x = var('x')
user_input = input("Enter Function - ")
expr = sympify(user_input)
r=[]
for i in y:
    res = expr.subs(x,i)
    r.append(res)
V = np.array(r,dtype=float)
plt.plot(y,V)
plt.show()

# setting up the eigenvalue matrix equation from finite difference
diag = V + 1/dy**2
off_diag = -1/(2*dy**2) * np.ones(len(diag)-1)
diag = np.array(diag,dtype=float)

ml2E,t = eigh_tridiagonal(diag,off_diag)
psi = t.T

num = int(input("How many wavefunctions?"))
leg = list()
for i in range(num):
    plt.plot(y,psi[i])
    leg.append(str(i))


plt.title("Energy Eigenstates -")
plt.xlabel('$y = x/L$')
plt.ylabel('$\psi$')
plt.grid()
plt.legend(leg)g
plt.show()