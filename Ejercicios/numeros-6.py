#Escribe un programa que pida al usuario un número y muestre por pantalla si es positivo, negativo o cero.
n1=input("Número: ")
try:
    n1 = int(n1)
    resul=n1
    if n1<0:
        print(f'{n1} es negativo')
    elif n1==0:
        print(f'{n1} es cero') 
    else:
        print(f'{n1} es positivo')  
except ValueError:
    print("numero no valido")