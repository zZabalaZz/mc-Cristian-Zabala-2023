import numpy as np

# Datos de la tabla
x1 = [1, 1, 2, 3, 1, 2, 3, 3]
x2 = [0, 1, 1, 2, 2, 3, 3, 1]
y = [1.6, 3, 1.1, 1.3, 3.2, 3.3, 1.8, 0]

# Ajuste de una función lineal generalizada
n = len(x1)
X = [[1, x1[i], x2[i]] for i in range(n)]
y = np.array(y)

# Coeficientes del modelo [a0, a1, a2]
coeffs = np.linalg.lstsq(X, y, rcond=None)[0]

# Imprimir los resultados
print("Función lineal ajustada:")
print("y =", coeffs[0], "+", coeffs[1], "x1 +", coeffs[2], "x2")

# Coeficiente de correlación (r)
y_pred = np.dot(X, coeffs)
residuals = y - y_pred
ss_residuals = sum(residuals**2)
ss_total = sum((y - np.mean(y))**2)
r = 1 - (ss_residuals / ss_total)
print(f"Coeficiente de correlación (r): {r:.4f}")
