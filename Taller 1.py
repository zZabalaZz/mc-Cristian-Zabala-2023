cant1=int(input("Ingrese la cantidad de elementos del conjunto A: "))
a=set()
c=set()
for i in range(cant1):
    dato=int(input("Ingrese un elemento: "))
    a.add(dato)
print("A = ",a,"\n")    

cant2=int(input("Ingrese la cantidad de elementos del conjunto B: "))
b=set()
for i in range(cant2):
    dato=int(input("Ingrese un elemento: "))
    b.add(dato)
print("B = ",b,"\n")

opc = 0
while(opc != 5):
    print("Operaciones posibles:\n"+"1. Unión de Conjuntos.\n"+"2. Intersección de Conjuntos.\n"+"3. Diferencia de conjuntos.\n"+"4. Diferencia Simétrica.\n"+"5. cerrar")
    opc=(int(input("Escoja una opción:")))
    if opc==1:
        a|=b
        print("A = ",a,"\n")
        
    elif opc==2:
        c=a&b
        if len(c)!=0:
            print("A & B = ",c)
        else:
            print("A & B = {}")
        
    elif opc==3:
        z=int(input("1. A-B.\n"+"2. B-A\n"+"3. Volver al menú anterior.\n"))
        while(z!=3):
            if z==1:
                a-=b
                print(a)
                
            elif z==2:
                b-=a
                print(b)
                             
            else:
                print("Escoja una opción valida:")                
            
    elif opc==4:
        a^=b
        print("A = ",a)
        
    else:
        print("Escoja una opción valida")