import math

import sympy

print(math.sqrt(9))
print(math.sqrt(8))

print(sympy.sqrt(8))

from sympy import symbols

x, y = symbols('x y')
expr = x + 2 * y
print(expr)

print(expr + 1)
print(expr - x)

print(x * expr)

from sympy import expand, factorial

expanded_expr = expand(x * expr)
print('Expanded Expression:', expanded_expr)

factorial_expr = factorial(x * expr)
print('Factorial Expression:', factorial_expr)
