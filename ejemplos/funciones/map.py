# map ejecutar una función a toda una lista
lista = ["1","2","3","4"]
print(sum, lista)
lista2 = list(map(int, lista))
print(lista2)
print (sum(lista2))
def cuadrado(x): return x**2
print(list(map(cuadrado, lista2)))