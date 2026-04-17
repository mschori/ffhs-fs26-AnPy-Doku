from sympy import *

x = Symbol('x')

f = 10 * x ** 3 + 20 * x + 30
diff(f, x)

g = x ** 2 * sin(x)
diff(g, x)

h = (x ** 2 + 1) / (x ** 3 + 1)
diff(h, x)

diff(tan(x), x)

diff(cot(x), x)

a = Symbol('a')
k = a ** x
diff(k, x)

ell = log(x, a)
diff(ell, x)

m = log(a, x)
diff(m, x)

n = cos(x ** 2)
diff(n, x)

q = Symbol('q')
p = sqrt(q(x))
diff(p, x)

r = log(q(x))
diff(r, x)

s = x ** x
diff(s, x)
