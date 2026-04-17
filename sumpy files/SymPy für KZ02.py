# SymPy importieren
import sympy as sp

# Symbol x definieren
x = sp.symbols('x')

# -----------------------------
# 1) Einfache Funktion anlegen
# -----------------------------
f = x**3 + 2*x**2 - 5*x + 7

print("Funktion f(x):")
print(f)

# Erste Ableitung berechnen
f_ableitung = sp.diff(f, x)

print("\nErste Ableitung f'(x):")
print(f_ableitung)

# Zweite Ableitung berechnen
f_zweite_ableitung = sp.diff(f, x, 2)

print("\nZweite Ableitung f''(x):")
print(f_zweite_ableitung)


# ----------------------------------------
# 2) Ableitung an einer Stelle auswerten
# ----------------------------------------
wert_an_2 = f_ableitung.subs(x, 2)

print("\nWert von f'(2):")
print(wert_an_2)


# ----------------------------------------
# 3) Exponentialfunktion ableiten
# ----------------------------------------
g = sp.exp(x)   # entspricht e^x

print("\nFunktion g(x):")
print(g)

g_ableitung = sp.diff(g, x)

print("\nAbleitung g'(x):")
print(g_ableitung)


# ----------------------------------------
# 4) Sinusfunktion ableiten
# ----------------------------------------
h = sp.sin(x)

print("\nFunktion h(x):")
print(h)

h_ableitung = sp.diff(h, x)

print("\nAbleitung h'(x):")
print(h_ableitung)


# ----------------------------------------
# 5) Produkt / Quotient / Wurzel
# ----------------------------------------
p = (x**2 + 1) * sp.sin(x)

print("\nFunktion p(x):")
print(p)

p_ableitung = sp.diff(p, x)

print("\nAbleitung p'(x):")
print(p_ableitung)

q = sp.sqrt(x) / (x + 1)

print("\nFunktion q(x):")
print(q)

q_ableitung = sp.diff(q, x)

print("\nAbleitung q'(x):")
print(q_ableitung)


# ----------------------------------------
# 6) Ergebnis schöner darstellen
# ----------------------------------------
print("\nVereinfachte Ableitung von q(x):")
print(sp.simplify(q_ableitung))


# ----------------------------------------
# 7) Allgemeine Funktion mit Parameter
# ----------------------------------------
a = sp.symbols('a', positive=True)
r = a**x

print("\nFunktion r(x):")
print(r)

r_ableitung = sp.diff(r, x)

print("\nAbleitung r'(x):")
print(r_ableitung)
# Erwartet: log(a)*a**x


# ----------------------------------------
# 8) Beispiel mit 10^x
# ----------------------------------------
s = 10**x

print("\nFunktion s(x):")
print(s)

s_ableitung = sp.diff(s, x)

print("\nAbleitung s'(x):")
print(s_ableitung)
# Erwartet: log(10)*10**x


# ----------------------------------------
# 9) Funktion und Ableitung zusammen
# ----------------------------------------
u = x**4 - 3*x**2 + 1
u_ableitung = sp.diff(u, x)

print("\nFunktion u(x):", u)
print("Ableitung u'(x):", u_ableitung)

# Wert an x = 1 einsetzen
print("u'(1) =", u_ableitung.subs(x, 1))