import re
import math

def seno(x, n):
    seno = 0
    for i in range(n):
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        seno += termino
    return seno

def coseno(x, n):
    resultado = 0.0
    for i in range(n):
        termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        resultado += termino
    return resultado

def tangente(x, n):
    tangente = 0
    for i in range(n):
        coeficiente = (-1) ** i
        numerador = x ** (2 * i + 1)
        denominador = math.factorial(2 * i + 1)
        termino = coeficiente * (numerador / denominador)
        tangente += termino
    return tangente



entrada_usuario = input("Ingresa una cadena con el formato 'función(argumento)': ")

# Definimos el patrón de expresión regular para buscar la función y el argumento
patron = r'([a-zA-Z]+)\((-?\d+)\)'

# Buscamos las coincidencias en la entrada del usuario
coincidencias = re.match(patron, entrada_usuario)

if coincidencias:
    funcion = coincidencias.group(1).lower()
    argumento = int(coincidencias.group(2))
    print("Función:", funcion)
    print("Argumento:", argumento)

    if funcion == "sen":
        resultado = seno(argumento, 30)
        print(f"El Seno de {argumento} es aproximadamente {resultado}")
    elif funcion == "cos":
        resultado = coseno(argumento, 30)
        print(f"El Coseno de {argumento} es aproximadamente {resultado}")
    elif funcion == "tan":
        resultado = tangente(argumento, 30)
        print(f"La Tangente de {argumento} es aproximadamente {resultado}")
    elif funcion == "csc":
        resultado = seno(argumento, 30)
        print(f"La Cosecante de {argumento} es aproximadamente {1/resultado}")
    elif funcion == "sec":
        resultado = coseno(argumento, 30)
        print(f"La Secante de {argumento} es aproximadamente {1/resultado}")
    elif funcion == "cot":
        resultado = tangente(argumento, 30)
        print(f"La Cotangente de {argumento} es aproximadamente {1/resultado}")
    else:
        print("Función no válida. Las funciones válidas son: sen, cos, tan, csc, sec, cot")
else:
    print("La entrada no coincide con el formato esperado.")
