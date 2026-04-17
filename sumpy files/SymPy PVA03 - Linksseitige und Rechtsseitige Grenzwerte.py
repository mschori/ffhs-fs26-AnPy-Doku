import numpy as np
import matplotlib.pyplot as plt
import sympy

# Graphische Darstellung und Limites von cot:

xp = np.linspace(0.05, np.pi-0.05)
xn = -xp

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect(1)
ax.set_xlim((-3,3))
ax.set_ylim((-3,3))
ax.plot([-3,3], [0,0], 'k')
ax.plot([0,0], [-3,3], 'k')

ax.plot(xp, 1 / np.tan(xp), 'r')
ax.plot(xn, 1 / np.tan(xn), 'r')

ax.set_title("Graph von $\cot$")

# Berechnung der Limites bei x = 0 mit Sympy:

x = sympy.Symbol('x')
print(sympy.limit(1/sympy.tan(x), x, 0, '+'))
print(sympy.limit(1/sympy.tan(x), x, 0, '-'))


# ---
# Graphische Darstellung und Limites von 1/x:

xp = np.linspace(0.05, 3, 100)
xn = -xp

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect(1)

ax.set_xlim((-3,3))
ax.set_ylim((-3,3))
ax.plot([-3,3], [0,0], 'k')
ax.plot([0,0], [-3,3], 'k')

ax.plot(xp, 1 / xp, 'r')
ax.plot(xn, 1 / xn, 'r')

ax.set_title("Graph von $1/x$")

# Berechnung der Limites bei x = 0 mi Sympy:

print(sympy.limit(1/x, x, 0, '+'))
print(sympy.limit(1/x, x, 0, '-'))


# ---
# Graphische Darstellung und Limites von \frac{1}{e^{-1/x}}

xp = np.linspace(0.05, 3, 300)
xn = -xp

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect(1)
ax.set_xlim((-3,3))
ax.set_ylim((0,6))
ax.plot([-3,3], [0,0], 'k')
ax.plot([0,0], [0,6], 'k')

ax.plot(xp, 1 / np.exp(-1/xp), 'r')
ax.plot(xn, 1 / np.exp(-1/xn), 'r')

ax.set_title("Graph von $g$")

# Berechnung der Limites bei x = 0 mit Sympy:

print(sympy.limit(1/sympy.exp(-1/x), x, 0, '+'))
print(sympy.limit(1/sympy.exp(-1/x), x, 0, '-'))


# ---
# Graphische Darstellung und Limites von \frac{1}{1 + e^{-1/x}}

xp = np.linspace(0.05, 3, 300)
xn = -xp

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect(1)
ax.set_xlim((-3,3))
ax.set_ylim((-0.5,1.5))
ax.plot([-3,3], [0,0], 'k')
ax.plot([0,0], [-0.5,1.5], 'k')

ax.plot(xp, 1 / (1+np.exp(-1/xp)), 'r')
ax.plot(xn, 1 / (1+np.exp(-1/xn)), 'r')

ax.set_title("Graph von $h$")

# Berechnung der Limites bei x = 0 mit Sympy:

print(sympy.limit(1/(1+sympy.exp(-1/x)), x, 0, '+'))
print(sympy.limit(1/(1+sympy.exp(-1/x)), x, 0, '-'))