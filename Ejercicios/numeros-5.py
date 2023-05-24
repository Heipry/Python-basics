#Escribe un programa que pida al usuario un número y calcule su factorial
n1=input("Número: ")
try:
    n1 = int(n1)
    resul=n1
    for x in (range(2, n1)):
        resul *= x
    print(resul)    
except ValueError:
    print("numero no valido")