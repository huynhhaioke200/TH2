from sympy import Limit, Symbol
x = Symbol('x')
Limit(1/x,  x,0, dir='–').doit()
Limit(1/x, x, 0, dir='+').doit()