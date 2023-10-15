import matplotlib.pyplot as plt
import numpy as np
import math

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.2, 0.5, 1.8, 3.4, 5.7, 9, 13.8])

zx = 0
zy = 0
xy = []
zxy = 0
x2 = []
zx2 = 0
st=[]

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

zxy8 = n * zxy
zxzy = zx * zy
zx28 = n * zx2
zxc = zx * zx


a1 = (zxy8 - zxzy) / (zx28 - zxc)
a0 = py - (a1 * px)

for i in y:
    st.append((i - py) ** 2)

st_total = sum(st)

sr = sum((y[i] - a0 - a1 * x[i]) ** 2 for i in range(len(x)))

sy=math.sqrt(st_total/6)

sysx=math.sqrt(sr/5)

r2=(st_total-sr)/st_total

r=math.sqrt(r2)*100

print("El valor de a1 es:", a1, "\nEl valor de a0 es:", a0,"\nLa desviación estandar es de:", sy,"\nEl error estándar de la estimación es de:",sysx,"\nY el coeficinte de correlacion es de:",r)


x_line = np.linspace(min(x), max (x), 100)
y_line = a1 * x_line + a0

plt.scatter(x, y, label='Puntos', color='blue')
plt.plot(x_line, y_line, label='Regresión Lineal', color='red')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.show()
