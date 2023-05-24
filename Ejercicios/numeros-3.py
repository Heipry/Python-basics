#Escribe un programa que pida al usuario un número y muestre por pantalla si es par o impar.
n1=input("Número: ")
try:
    n1 = int(n1)
    if n1%2 ==0:
        print (f'{n1} es par')
    else:
        print (f'{n1} es impar')

except ValueError:
    print("numero no valido")