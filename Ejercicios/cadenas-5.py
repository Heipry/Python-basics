#Escribe un programa que pida al usuario una cadena de texto y muestre por pantalla si la palabra "python" está en ella.
frase = input("Escribe una frase: ")
frase_minus = frase.lower()
if "python" in frase_minus:
    print("La palabra python está en "+ frase)
else:
    print("La palabra python NO está en "+ frase)
