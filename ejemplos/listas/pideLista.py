try:
    numero = int(input("Dame un primer numero positivo: "))
    lista = [numero]
    while numero>=0:        
        try:           
            numero = int(input("Dame otro numero (negativo para terminar): "))
            lista.append(numero)
        except:
            print("numero no valido, vuelve a intentarlo")
    lista.pop()
    print(f'El mayor es {max(lista)}')
    print("Y los numeros pares introducidos han sido: ", end=" ")
    for i in lista:    
        if i%2==0:
            print(str(i), end=" ")
    print()
    lista_inv = lista.copy()
    lista_inv.reverse()
    print(f"La lista invertida es: {lista_inv}")
    lista_ord = lista.copy()
    lista_ord.sort()    
    if lista == lista_ord:
        print("la lista está ordenada")
    else:
        print(f"La lista {lista} no está ordenada")
    
except:
    print("numero no válido, abortamos programa")