# Usando bucles dentro de corchetes podemos crear listas reducidas con el mismo resultado que las funciones predefinidas
# map
lista = [ "1","2","3","4","5"]
print(lista)
lista2 = [int(x) for x in lista]
print(lista2)
#filter
lista3 = [x for x in lista2 if x%2==0]
print(lista3)
#operaciones con matrices
lista4=[x + y for x in lista2 for y in lista3]
print(lista4)