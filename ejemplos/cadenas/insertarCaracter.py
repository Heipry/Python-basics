frase = input("Introduce una frase: ")
caracter = input("Introduce separador: ")

nuevafrase="";
for letra in frase:
    nuevafrase += letra+caracter
print(nuevafrase)


fraseJoin = caracter.join(frase)
print(fraseJoin)
