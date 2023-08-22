a=float(input("Ingrese un valor: "))
import math
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
        cos+=(a**z)/math.factorial(z)
    else:
        cos-=(a**z)/math.factorial(z)
    z+=2
    it+=1
    ea=abs((cos-ant)/cos)*100
        
print("COS: ",cos,"Ea: ",ea,"la cantidad de iteracioes es:", it)