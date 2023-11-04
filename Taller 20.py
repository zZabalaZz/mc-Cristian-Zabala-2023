import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5, 6]
y = [3.2, 0.4, -1, -1.4, -1.1, 0.6, 3.1]

coefficients = np.polyfit(x, y, 2)
a, b, c = coefficients

x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * x_fit ** 2 + b * x_fit + c

r = np.corrcoef(y, a * np.array(x) ** 2 + b * np.array(x) + c)[0, 1]

print("Coeficientes del polinomio de segundo grado:")
print("a =", a)
print("b =", b)
print("c =", c)

print("Coeficiente de correlación (r):", r)

plt.scatter(x, y, label="Datos")

plt.plot(x_fit, y_fit, label="Polinomio de 2do grado", color='red')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()
