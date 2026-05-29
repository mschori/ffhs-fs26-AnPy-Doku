import sympy as sp
from IPython.display import display, Math

# =========================================================
# SYMBOL
# =========================================================

x = sp.symbols('x')

# =========================================================
# HILFSFUNKTIONEN
# =========================================================

def show(txt):
    display(Math(txt))

def line():
    print("=" * 80)

# =========================================================
# POTENZREGEL ERKENNEN
# =========================================================

def extract_power(term):

    coeff = 1

    # z.B. 5*x^2
    if term.is_Mul:

        coeffs = []
        powers = []

        for arg in term.args:

            if arg.has(x):
                powers.append(arg)
            else:
                coeffs.append(arg)

        if len(powers) == 1:

            coeff = sp.Mul(*coeffs)

            power_expr = powers[0]

            if power_expr == x:
                return coeff, 1

            if power_expr.is_Pow and power_expr.base == x:
                return coeff, power_expr.exp

    # z.B. x^5
    if term == x:
        return 1, 1

    if term.is_Pow and term.base == x:
        return 1, term.exp

    # Konstante
    if not term.has(x):
        return term, 0

    return None, None

# =========================================================
# EINZELNES INTEGRAL ERKLÄREN
# =========================================================

def integrate_term_verbose(term):

    show(r"\int " + sp.latex(term) + r"\,dx")

    coeff, power = extract_power(term)

    # -----------------------------------------------------
    # POTENZREGEL
    # -----------------------------------------------------

    if power is not None:

        print("Potenzregel erkannt")
        print()

        if power == -1:

            print("Spezialfall:")
            print("∫1/x dx = ln|x| + C")

            result = sp.log(sp.Abs(x))

            show(sp.latex(result))

            return result

        new_exp = power + 1

        print("Exponent um 1 erhöhen:")

        show(
            sp.latex(power)
            + "+1="
            + sp.latex(new_exp)
        )

        print()

        print("Durch neuen Exponenten teilen:")

        result = coeff * x**new_exp / new_exp

        show(sp.latex(result))

        return result

    # -----------------------------------------------------
    # STANDARD-INTEGRATION
    # -----------------------------------------------------

    print("Standardintegration")

    result = sp.integrate(term, x)

    show(sp.latex(result))

    return result

# =========================================================
# STAMMFUNKTION BILDEN
# =========================================================

def build_antiderivative(expr_str):

    expr = sp.sympify(expr_str)

    line()
    print("STAMMFUNKTION BILDEN")
    line()

    print()

    show(r"f(x)=" + sp.latex(expr))

    print()

    print("Gesucht: Stammfunktion F(x)")
    print()

    expanded = sp.expand(expr)

    # -----------------------------------------------------
    # AUSMULTIPLIZIEREN
    # -----------------------------------------------------

    if expanded != expr:

        print("Schritt 1: Ausdruck ausmultiplizieren")
        print()

        show(
            sp.latex(expr)
            + "="
            + sp.latex(expanded)
        )

        expr = expanded

        print()

    terms = expr.as_ordered_terms()

    # -----------------------------------------------------
    # LINEARITÄT
    # -----------------------------------------------------

    if len(terms) > 1:

        print("Schritt 2: Integral aufteilen")
        print()

        parts = []

        for term in terms:

            parts.append(
                r"\int "
                + sp.latex(term)
                + r"\,dx"
            )

        show("=" + "+".join(parts))

        print()

    # -----------------------------------------------------
    # EINZELNE TERME
    # -----------------------------------------------------

    print("Schritt 3: Einzelne Stammfunktionen")
    print()

    partial_results = []

    for term in terms:

        result = integrate_term_verbose(term)

        partial_results.append(result)

        print()

    # -----------------------------------------------------
    # ZUSAMMENFÜHREN
    # -----------------------------------------------------

    print("Schritt 4: Zusammenführen")
    print()

    final_result = sp.simplify(sum(partial_results))

    show(
        r"F(x)="
        + sp.latex(final_result)
        + "+C"
    )

    print()

    # -----------------------------------------------------
    # KONTROLLE
    # -----------------------------------------------------

    print("Kontrolle durch Ableiten")
    print()

    derivative = sp.diff(final_result, x)

    show(
        r"\frac{d}{dx}\left("
        + sp.latex(final_result)
        + r"\right)="
        + sp.latex(derivative)
    )

    if sp.simplify(derivative - expr) == 0:
        print("✓ Kontrolle korrekt")
    else:
        print("✗ Kontrolle fehlgeschlagen")

# =========================================================
# UNBESTIMMTES INTEGRAL
# =========================================================

def solve_indefinite_integral(expr_str):

    expr = sp.sympify(expr_str)

    line()
    print("UNBESTIMMTES INTEGRAL")
    line()

    print()

    show(
        r"\int "
        + sp.latex(expr)
        + r"\,dx"
    )

    print()

    build_antiderivative(expr_str)

# =========================================================
# BESTIMMTES INTEGRAL
# =========================================================

def solve_definite_integral(expr_str, lower, upper):

    expr = sp.sympify(expr_str)

    line()
    print("BESTIMMTES INTEGRAL")
    line()

    print()

    show(
        r"\int_{"
        + sp.latex(lower)
        + r"}^{"
        + sp.latex(upper)
        + r"}"
        + sp.latex(expr)
        + r"\,dx"
    )

    print()

    # -----------------------------------------------------
    # STAMMFUNKTION
    # -----------------------------------------------------

    print("Schritt 1: Stammfunktion bilden")
    print()

    antiderivative = sp.integrate(expr, x)

    show(
        r"F(x)="
        + sp.latex(antiderivative)
    )

    print()

    # -----------------------------------------------------
    # HAUPTSATZ
    # -----------------------------------------------------

    print("Schritt 2: Hauptsatz anwenden")
    print()

    show(
        r"\int_a^b f(x)\,dx = F(b)-F(a)"
    )

    print()

    # -----------------------------------------------------
    # OBERE GRENZE
    # -----------------------------------------------------

    print("Schritt 3: Obere Grenze einsetzen")
    print()

    upper_value = antiderivative.subs(x, upper)

    show(
        r"F("
        + sp.latex(upper)
        + r")="
        + sp.latex(upper_value)
    )

    print()

    # -----------------------------------------------------
    # UNTERE GRENZE
    # -----------------------------------------------------

    print("Schritt 4: Untere Grenze einsetzen")
    print()

    lower_value = antiderivative.subs(x, lower)

    show(
        r"F("
        + sp.latex(lower)
        + r")="
        + sp.latex(lower_value)
    )

    print()

    # -----------------------------------------------------
    # SUBTRAHIEREN
    # -----------------------------------------------------

    print("Schritt 5: Subtrahieren")
    print()

    result = sp.simplify(
        upper_value - lower_value
    )

    show(
        sp.latex(upper_value)
        + "-"
        + sp.latex(lower_value)
    )

    print()

    show(
        "="
        + sp.latex(result)
    )

    print()

    # -----------------------------------------------------
    # ENDERGEBNIS
    # -----------------------------------------------------

    line()
    print("ENDERGEBNIS")
    line()

    show(
        r"\int_{"
        + sp.latex(lower)
        + r"}^{"
        + sp.latex(upper)
        + r"}"
        + sp.latex(expr)
        + r"\,dx="
        + sp.latex(result)
    )

# =========================================================
# NUR STAMMFUNKTION
# =========================================================

def antiderivative(expr_str):

    expr = sp.sympify(expr_str)

    line()
    print("STAMMFUNKTION")
    line()

    result = sp.integrate(expr, x)

    show(
        r"F(x)="
        + sp.latex(result)
        + "+C"
    )

# =========================================================
# TESTS
# =========================================================

# ---------------------------------------------------------
# STAMMFUNKTION
# ---------------------------------------------------------

# antiderivative("x**2")

# ---------------------------------------------------------
# UNBESTIMMTES INTEGRAL
# ---------------------------------------------------------

solve_indefinite_integral("x")

# solve_indefinite_integral("3*x**2 + 2*x + 1")

# solve_indefinite_integral("x**5")

# solve_indefinite_integral("1/x")

# ---------------------------------------------------------
# BESTIMMTES INTEGRAL
# ---------------------------------------------------------

# solve_definite_integral("x**2", 0, 2)

# solve_definite_integral("3*x**2 + 2*x", 1, 4)