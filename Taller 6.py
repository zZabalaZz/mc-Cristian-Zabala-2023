a=float(input("Ingrese el valor(en radianes) a calcular coseno: "))
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado
es=(0.5*10**-8)*100
print(es)
ea=100
cos=0 #cos jajajaj
it=0
z=0
while ea>=es:
    ant=cos
    if it%2==0:    
        cos+=(a**z)/factorial(z)
    else:
        cos-=(a**z)/factorial(z)
    z+=2
    it+=1
    ea=abs((cos-ant)/cos)*100
        
print("El valor estimado del coseno de",z,"es: ",cos,"El error aproximado relativo porcentual es: ",ea,"Y la cantidad de iteracioes es:", it)
