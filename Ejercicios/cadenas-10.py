# Escribe un programa que pida al usuario una cadena de texto y muestre por pantalla si
# es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# izquierda).
frase = input("Escribe una frase: ")
frase2 = frase[::-1]
if frase==frase2:
    print(f'{frase} es un palíndromo')
else:
    print(f'{frase} NO es un palíndromo')
    frase_limpia = frase.replace(" ", "")
    frase2_limpia = frase2.replace(" ", "")
    if frase_limpia == frase2_limpia:
        print(f'Pero si nos olvidamos de los espacios {frase_limpia} sí lo sería')


 