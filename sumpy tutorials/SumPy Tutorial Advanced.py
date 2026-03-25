from sympy import *

x, t, z, nu = symbols('x t z nu')

# Will make all further examples pretty print with unicode characters.
init_printing(use_unicode=True)

diff(sin(x)*exp(x),x)

integrate(exp(x)*sin(x) + exp(x)*cos(x), x)

integrate(sin(x**2), (x, -oo, oo))

latex(Integral(cos(x)**2, (x, 0, pi)))