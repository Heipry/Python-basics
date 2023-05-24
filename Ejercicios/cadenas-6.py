#Escribe un programa que pida al usuario una cadena de texto y muestre por pantalla si la longitud de la cadena es impar o par.
frase = input("Escribe una frase: ")

if len(frase)%2==0:
    print(f'{frase} tiene un número de caracteres par: {len(frase)}')
else:
    print(f'{frase} tiene un número de caracteres impar: {len(frase)}')