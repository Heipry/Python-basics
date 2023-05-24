saludo = ["Hola","usuario", "buenas","tardes","bienvenido","usuario","aquí",]
palabra = input("Dime la palabra: ")
print(f"La palabra {palabra} está en la lista? ", end=" ")
if palabra in saludo:
    print("sí, un total de ", end=" ")
    veces = saludo.count(palabra)
    print(veces, "veces")
   
    palabra2 = input("Dime la palabra de sustitución: ")
    for i in range(0, veces):
        pos =saludo.index(palabra)
        saludo[pos] = palabra2
       # saludo.insert(saludo.index(palabra), palabra2)
        # saludo.remove(palabra)   
    print(saludo)
else:
    print("no")