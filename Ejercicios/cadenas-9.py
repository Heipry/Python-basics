#Escribe un programa que pida al usuario una cadena de texto y muestre por pantalla cuántas palabras tiene la cadena.
frase = input("Escribe una frase larga: ")
print(f'La frase tiene {len(frase.split())} palabras')