frase = input("Frase: ")
#palindromo por letras
palabras = frase.split(" ")
palabras_r = palabras[::-1]
if palabras == palabras_r:
    print(palabras, "es una frase palindromo")
else:
    print(palabras, "no es una frase palindromo")