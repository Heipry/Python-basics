frase = input("Introduce una frase: ")

lista = frase.lower().split()
lista_invertida = lista[::-1]

print("es un palindromo" if lista==lista_invertida  else "no es un palindromo")