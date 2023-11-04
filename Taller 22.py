x_values = [0, 1, 2, 3, 4]
y_values = [1, 0.2, 2, 4.2, 5]
x_to_estimate = 2.5

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result



f_2_5_degree_1 = lagrange_interpolation(x_values[:2], y_values[:2], x_to_estimate)
f_2_5_degree_2 = lagrange_interpolation(x_values[:3], y_values[:3], x_to_estimate)
f_2_5_degree_3 = lagrange_interpolation(x_values, y_values, x_to_estimate)

def degree_1_polynomial(x):
    x0, x1 = x_values[:2]
    y0, y1 = y_values[:2]
    m = (y1 - y0) / (x1 - x0)
    b = y0 - m * x0
    return m * x + b

def degree_2_polynomial(x):
    x0, x1, x2 = x_values[:3]
    y0, y1, y2 = y_values[:3]
    a0 = y0
    a1 = (y1 - y0) / (x1 - x0)
    a2 = ((y2 - y0) / (x2 - x0) - a1) / (x2 - x1)
    return a0 + a1 * (x - x0) + a2 * (x - x0) * (x - x1)

print(f"Estimación de f(2.5) con polinomio de grado 1: {f_2_5_degree_1}")
print(f"Estimación de f(2.5) con polinomio de grado 2: {f_2_5_degree_2}")
print(f"Estimación de f(2.5) con polinomio de grado 3: {f_2_5_degree_3}")

print(f"Polinomio de grado 1 asociado a los primeros dos puntos: f(x) = {degree_1_polynomial(x_to_estimate)}")
print(f"Polinomio de grado 2 asociado a los primeros tres puntos: f(x) = {degree_2_polynomial(x_to_estimate)}")
