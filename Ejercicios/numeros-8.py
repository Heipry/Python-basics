#Escribe un programa que pida al usuario tres números y muestre por pantalla el menor de ellos.
n1=input("Primer numero: ")
n2=input("Segundo numero: ")
n3=input("Tercer numero: ")
try:
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    lista = [n1,n2,n3]
    lista.sort()
    print(lista[0])
except ValueError:
    print("Los valores no son válidos")