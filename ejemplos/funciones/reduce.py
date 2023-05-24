# reduce obtener un dato acumulado al ejecutar la función en una lista
from functools import reduce

def add(x,y): return x+y
lista = [1,2,3,4,5]
print(lista)
resultado = reduce(add,lista)
print(resultado)