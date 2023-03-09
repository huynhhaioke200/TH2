from sympy import *
x = Symbol('x')
eq = (1+1/x)/(x-1)
from sympy.solvers.solvers import denoms
loai_tru = set()
for d in denoms(eq):
    for s in solve(d):
        loai_tru.add(s)
print(loai_tru)