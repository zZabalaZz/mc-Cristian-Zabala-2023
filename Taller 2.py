def union(a,b):
    c=a|b
    return c

def dif(a,b):
    c=a-b
    return c

def int(a,b):
    c=a&b
    return c

def sim(a,b):
    c=a^b
    return c

A=set()
X=set()
Y=set()
Z=set()
for i in range (26):
    if i%2==1:
        A.add(i)
print("A = ",A)

B=set()
for i in range(21):
    if i>=6 and i<20:
        B.add(i)
print("B = ",B)

C={1,4,7,8,12,16,18,21}
print("C = ",C)

D=set()
for i in range(2, 51):
    primos = True
    for j in range(2,i):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        D.add(i)  
print("D = ",D)


X=sim(B,D)
Z=int(A,X)
print("𝐴 ⋂(𝐵⨁𝐷): ",Z)
Z=set()
X=set()

###

X=int(B,C)
Z=union(X,D)
print("(𝐵⋂𝐶) ⋃ D: ",Z)
Z=set()
X=set()

###

X=union(A,C)
Z=dif(X,B)
print("(𝐴⋃𝐶) − B: ",Z)
Z=set()
X=set()

###

X=dif(B,C)
Y=int(A,C)
Z=sim(X,Y)
print("(𝐵−𝐶)⨁(𝐴⋂C): ",Z)
