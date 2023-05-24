#Escribe un programa que pida al usuario un número y muestre por pantalla su tabla de multiplicar del 1 al 10.
n1=input("Número: ")
try:
    n1 = int(n1)
    for x in range(1, 11):
        resul = n1 * x
        print(F'{n1} x {x} = {n1*x}')
except ValueError:
    print("numero no valido")
