frase = input("Introduce una frase: ")
palabra = input("Introduce una palabra: ")
if frase.count(palabra) >0:
    print(palabra, " existe en ", frase)
else:
    print(palabra, " no existe en ", frase)
print(frase if frase<palabra else palabra, "va alfabeticamente antes")




