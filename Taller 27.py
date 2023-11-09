def f(x):
    return 1.5 * x**3 - 3.5 * x**2 - 2 * x + 2

def bisection_method(a, b, tol, max_iter):
    iteration = 0

    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    root = (a + b) / 2
    error = (b - a) / 2

    return root, error, iteration

# Parámetros iniciales
a = -10
b = 10
tolerance = 1e-8
max_iterations = 1000

# Llamada al método de bisección
result = bisection_method(a, b, tolerance, max_iterations)

# Resultado
print(f"Raíz aproximada: {result[0]:.8f}")
print(f"Error aproximado: {result[1]:.8f}")
print(f"Número de iteraciones: {result[2]}")