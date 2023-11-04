def lagrange_interpolation(x_values, y_values):
    n = len(x_values)
    result = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Puntos de ejemplo
x_values = [0, 1, 2, 3, 4]
y_values = [1, 0.9, -1, -2.3, 1.8]

# Valor para el que deseas encontrar la interpolación
x = 2.5

result = lagrange_interpolation(x_values, y_values)

print(f"El valor interpolado en x={x} es f({x}) = {result}")
