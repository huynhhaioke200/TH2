from sympy import *
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
from sympy.solvers.solvers import denoms
eq = 1/(x**2-4)+2/((y**2)+(5*y)-6)-3/((z**2)-9)
loai_tru = set()
for d in denoms(eq):
    for s in solve(d):
        loai_tru.add(s)
print(loai_tru)