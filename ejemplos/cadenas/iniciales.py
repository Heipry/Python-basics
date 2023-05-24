frase = input("Introduce una frase: ")
#mostrar iniciales
print("Las iniciales son:", end=" ")
frase_partida = frase.split()
for palabra in frase_partida:
    print(palabra[0], end="")
print()
#mostrar frase con primeras letras mayusculas
print("La frase es:")
frase_mayus = frase.title()
print(frase_mayus)
# Palabras que comienzan con letra a
print("las palabras que empiezan por a son: ", end=" ")
for palabra in frase_partida:
    if palabra.startswith("a") or palabra.startswith("A"):
        print(palabra, end=" ")
print()