frase = input("Dime tu frase: ")
lista_palabras =frase.split()
palabras = {}
for p in lista_palabras:
    palabras.setdefault(p,0)
    palabras[p]=palabras[p]+1

print(palabras)