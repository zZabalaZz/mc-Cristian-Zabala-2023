a = float(input("Ingrese el valor a calcular: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)

es = (0.5 * 10**-8) * 100
print(es)

ea = 100
e = 0
it = 0
z = 0

while ea >= es:
    ant = e
    if it % 2 == 0:
        e += (a ** z) / factorial(z)
    else:
        e -= (a ** z) / factorial(z)
    z += 1
    it += 1
    ea = abs((e - ant) / e) * 100

z = 0
e2 = 0
it2 = 0
ea2 = 100

while ea2 >= es:
    ant2 = e2
    e2 +=  (a ** z) / factorial(z)
    z += 1
    it2 += 1
    ea2 = abs((e2 - ant2) / e2) * 100

print("Por la primera aproximación\n" + "El valor estimado: ", e, "\nEl error aproximado relativo porcentual es: ",
      ea, "\nY la cantidad de iteraciones es:", it, "\nPor la segunda aproximación:\n" + "El valor estimado: ", 1/e2,
      "\nEl error aproximado relativo porcentual es: ", ea2, "\nY la cantidad de iteraciones es:", it2)
