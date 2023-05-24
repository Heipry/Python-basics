#Escribe un programa que pida al usuario dos números y muestre por pantalla su suma, resta, multiplicación y división.
n1=input("Primer numero:")
n2=input("Segundo numero:")
try:
    n1=int(n1)
    n2=int(n2)
    suma = n1+n2
    resta = n1-n2
    multiplicacion = n1*n2
    if n2!=0:
        division = n1/n2
    else: 
        division = "infinito"
    print("La suma es " + str(suma))
    print("La resta es " + str(resta))
    print("La multiplicación es "+ str(multiplicacion))
   # print("La división es "+ str(division))
    print("La división es", division)
except ValueError:
    print("Los valores no son válidos")


    

