#Escribe un programa que pida al usuario dos números y muestre por pantalla el mayor de ellos.
n1=input("Primer numero: ")
n2=input("Segundo numero: ")
try:
    n1=int(n1)
    n2=int(n2)
    if n1<n2:
        print(f'{n2} es mayor')
    elif n1==n2:
        print(f'{n1} y {n2} son iguales') 
    else:
        print(f'{n1} es mayor') 
except ValueError:
    print("Los valores no son válidos")