import random

def pidenumero():
    numero = input("Adivina un numero entre 0 y 100: ")
    try:
        numero = int(numero)
        return numero
    except:
        print(numero + " no es válido como numero entre 0 y 100")

num_final = random.randint(0,101)
num_usuario = pidenumero()
contador = 1
while num_final != num_usuario: 
    if  num_usuario != None:
        if  num_final<num_usuario:
            print("Has fallado! el número es menor")
        else:
            print("Has fallado! el número es mayor")
    num_usuario = pidenumero()  
    contador+=1
print(f"Enhorabuena, el numero era el {num_final} y acertaste en {contador} intentos")





