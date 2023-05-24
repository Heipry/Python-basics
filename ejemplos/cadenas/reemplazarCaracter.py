frase = input("Introduce una frase: ")
caracter = input("Introduce mascara: ")
for numero in range(10):
    frase=frase.replace(str(numero),caracter)
print(frase)
