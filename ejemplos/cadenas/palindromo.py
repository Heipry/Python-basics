palabra = input("Introduce una palabra: ")
palindromo = ""
for letra in palabra:
    palindromo = letra+palindromo
#palindromo = palabra[::-1]
print("es un palindromo" if palindromo==palabra  else "no es un palindromo")