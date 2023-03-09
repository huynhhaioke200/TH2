from sympy.solvers.solvers import denoms
from sympy import *
x = Symbol('x')
eq = (1/x)*1/(x-3)
dd = denoms(eq)
print(dd)