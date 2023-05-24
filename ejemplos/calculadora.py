def muestra_menu():
    print("-- CALCULADORA --")
    print("opciones: ")
    print("1 - Sumar dos numeros enteros")
    print("2 - Restar dos numeros enteros")
    print("3 - Multiplicar dos numeros enteros")
    print("4 - Dividir dos numeros enteros")
    print("0 - SALIR")
    try:        
        numero = input("Elige opción:")
        numero = int(numero)        
    except:
        print(numero + " no parece un número")
        numero = 10
    return numero      

def pide_numeros():
    n1 = input("Primer numero:")
    n2 = input("Segundo numero:")
    try:
        n1=int(n1)
        n2=int(n2)     
        return (n1,n2)  
    except:
        print("Los números no son válidos")        
   
opc = muestra_menu()
while opc != 0:   
        
    match opc:
        case 1:
            n = pide_numeros()
            if n is not None:
                print(f"\n{n[0]} + {n[1]} = {n[0]+n[1]}\n")

        case 2:
            n = pide_numeros()
            if n is not None:
                print(f"\n{n[0]} - {n[1]} = {n[0]-n[1]}\n")

        case 3:
            n = pide_numeros()
            if n is not None:
                print(f"\n{n[0]} x {n[1]} = {n[0]*n[1]}\n")

        case 4:
            n = pide_numeros()
            if n is not None:
                try:
                    print(f"\n{n[0]} / {n[1]} = {n[0]/n[1]}\n")
                except:
                    print(f"\n{n[0]} / {n[1]} no se puede dividir\n")

        case _:
            print(f"La opción no es válida\n")

    opc = muestra_menu()
print("Hasta la próxima")
            


