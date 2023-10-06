import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.2, 3, 4.5, 6, 8.5, 12])

y_log = np.log(y)


def modelo_lineal(x, a, b):
    return a + b * x

params, covariance = curve_fit(modelo_lineal, x, y_log)

a_estimado, b_estimado = params

a_original = np.exp(a_estimado)
b_original = b_estimado

print("Parámetros estimados:")
print("a =", a_original)
print("b =", b_original)

plt.scatter(x, y, label='Datos')
plt.plot(x, a_original * np.exp(b_original * x), color='red', label='Ajuste')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
