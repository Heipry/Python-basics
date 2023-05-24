comensales = {}
comensal = input("Nombre: ")
while comensal != "fin":
    plato = input("Plato que le gusta: ")
    gustos = comensales.setdefault(comensal, [plato])    
    anadir = True
    if plato not in gustos:
        gustos = gustos.append(plato)
    print(comensales)
    comensal = input("Nombre: ")