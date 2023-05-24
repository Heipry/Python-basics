# Escribe un programa que pida al usuario un número y muestre por pantalla si es un
# número perfecto o no. Un número perfecto es un número entero positivo que es igual
# a la suma de sus divisores propios positivos.
n1=input("Número: ")
try:
    n1 = int(n1)
    resul = 0
    for x in (range(1, n1)):        
        if n1%x == 0:
            resul += x
    if resul==n1:
        print(f'{n1} es un numero perfecto')  
    else:
        print(f'la suma de los divisores de {n1} es {resul}, así que no es perfecto')  

except ValueError:
    print("numero no valido")