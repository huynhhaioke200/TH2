from sympy import Limit, sin, Symbol
x = Symbol('x')
Limit(sin(x)/x, x, 0).doit()