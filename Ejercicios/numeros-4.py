#Escribe un programa que pida al usuario un número y muestre por pantalla si es primo o no.
n1=input("Número: ")
try:
    n1 = int(n1)
    
    for x in (range(2, n1)):
        
        if n1%x == 0:
            print (f'{n1} no es primo ya que es divisible por {x}')
            break
    if x+1==n1:
            print(f'{n1} es primo')    

except ValueError:
    print("numero no valido")