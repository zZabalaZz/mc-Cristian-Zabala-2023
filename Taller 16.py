import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [7, 5, 6, 3, 4, 2.5, 2, 0.5]
zx = 0
zy = 0
xy = []
zxy = 0
x2 = []
zx2 = 0


for i in range(len(x)):
    zx += x[i]
    zy += y[i]
    xy.append(x[i] * y[i])
    x2.append(x[i] * x[i])

for i in xy:
    zxy += i

for i in x2:
    zx2 += i


n = len(x)
px = zx / n
py = zy / n
#Me tocó hacer paso por paso una variable porque no me daba :'()
zxy8 = n * zxy
zxzy = zx * zy
zx28 = n * zx2
zxc = zx * zx

a1 = (zxy8 - zxzy) / (zx28 - zxc)
a0 = py - (a1 * px)

print("El valor de a1 es:", a1, "\n El valor de a0 es:", a0)


x_line = np.linspace(min(x), max(x), 100)
y_line = a1 * x_line + a0

plt.scatter(x, y, label='Puntos', color='blue')
plt.plot(x_line, y_line, label='Regresión Lineal', color='red')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.show()
