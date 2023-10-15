import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.2, 0.5, 1.8, 3.4, 5.7, 9, 13.8])
st=[]
y_log = np.log(y)
py = np.mean(y)

def modelo_lineal(x, a, b):
    return a + b * x

params, covariance = curve_fit(modelo_lineal, x, y_log)

a_estimado, b_estimado = params

a0 = np.exp(a_estimado)
a1 = b_estimado


for i in y:
    st.append((i - py) ** 2)

st_total = sum(st)

sr = sum((y[i] - a0 - a1 * x[i]) ** 2 for i in range(len(x)))

sy=math.sqrt(st_total/6)

sysx=math.sqrt(sr/5)

r2=(st_total-sr)/st_total

r=math.sqrt(r2)*100

print("El valor de a1 es:", a1, "\nEl valor de a0 es:", a0,"\nLa desviación estandar es de:", sy,"\nEl error estándar de la estimación es de:",sysx,"\nY el coeficinte de correlacion es de:",r)


plt.scatter(x, y, label='Datos')
plt.plot(x, a0 * np.exp(a1 * x), color='red', label='Ajuste')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
