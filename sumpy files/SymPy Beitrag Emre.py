import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.symbols('x')

# 🔹 Level 1 – Basics
# x^2
# x^3
# 5*x^4 - 2*x + 1
# sqrt(x)
# log(x)
# exp(x)

# 🔹 Level 2 – Kombinationen
# x^2 + log(x)
# x^2 * log(x)
# x * exp(x)
# sin(x) + cos(x)

# 🔹 Level 3 – Quotient
# x/(x^2 + 1)
# (2*x + 1)/(x^2 + 3)
# sin(x)/(x + 1)

# 🔹 Level 4 – Kettenregel
# sin(x^2)
# cos(3*x)
# sqrt(3*x^2 + 1)
# log(x^2 + 1)
# exp(x^2)

# 🔹 Level 5 – Kombiniert (Prüfungsniveau)
# x^2 * sin(x^3)
# exp(x^2 + 3*x)
# sin(2*x^2 + 3*x)
# (x^2 + 1)^5

# 🔹 Level 6 – Schwieriger
# sin(x)/x
# log(x)/x
# x^2/(sin(x) + 1)
# exp(x)/(x^2 + 1)

# 🔹 Level 7 – Perfekt für Plot + Tangente
# x^3 - 3*x
# sin(x)
# exp(x)
# x^2 * log(x)

# 🔹 Spezialfälle (Domain beachten)
# log(x)
# sqrt(x)
# 1/x

# 🔹 Bonus – Klassiker
# x^2 * exp(x)
# sin(x^2) * log(x)
# (x^3 + 1)/(x^2 + 1)
# exp(sin(x))


x = sp.symbols('x')

# 🔹 Auto-Fix + Speicherung Original
def fix_input(expr):
    original = expr  # 👈 merken für Anzeige
    expr = expr.lower()
    expr = expr.replace("^", "**")
    expr = expr.replace("ln(", "log(")
    expr = expr.replace("e^", "exp(")
    return original, expr


# 🔹 Berechnung + LaTeX
def berechne(expr_str):
    try:
        original_input, fixed_expr = fix_input(expr_str)

        f = sp.sympify(fixed_expr)
        f = f.doit()

        f_prime = sp.diff(f, x).doit()
        f_prime = sp.simplify(f_prime)

        print("\n📌 Original Input:")
        print(original_input)

        print("\n📌 Bereinigte Funktion:")
        sp.pprint(f)

        print("\n📌 Ableitung:")
        sp.pprint(f_prime)

        # 🔥 LATEX
        latex_f = sp.latex(f)
        latex_fp = sp.latex(f_prime)

        print("\n📐 LaTeX Darstellung:")
        print(f"$f(x) = {latex_f}$")
        print(f"$f'(x) = {latex_fp}$")

        # 🔥 Obsidian-ready Block
        print("\n📝 Obsidian Block:")
        print(f"## Funktion\n$f(x) = {latex_f}$\n")
        print(f"## Ableitung\n$f'(x) = {latex_fp}$")

        return f, f_prime

    except Exception as e:
        print("❌ Fehler:", e)
        return None, None


# 🔹 Plot
def plot(f, f_prime):
    try:
        f_l = sp.lambdify(x, f, 'numpy')
        f_p_l = sp.lambdify(x, f_prime, 'numpy')

        xs = np.linspace(-10, 10, 400)

        plt.figure(figsize=(10, 6))
        plt.plot(xs, f_l(xs), label="f(x)")
        plt.plot(xs, f_p_l(xs), '--', label="f'(x)")

        plt.axhline(0)
        plt.axvline(0)
        plt.grid()
        plt.legend()
        plt.title("Funktion & Ableitung")

        plt.show()

    except Exception as e:
        print("❌ Plot Fehler:", e)


# 🔹 MAIN
print("=== Sympy LaTeX Tool (Upgrade) ===")

expr = input("Gib Funktion ein: ")

f, f_prime = berechne(expr)

if f:
    choice = input("\nPlot anzeigen? (j/n): ")
    if choice.lower() == 'j':
        plot(f, f_prime)

print("\n=== Fertig ===")
