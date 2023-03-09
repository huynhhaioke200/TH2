from sympy import Limit, Symbol, S
x = Symbol('x')
Limit (1/x, x, S.Infinity)
gioi_han = Limit(1/x, x, S.Infinity)
gioi_han.doit()