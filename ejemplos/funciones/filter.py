# filter elegir de una lista solo los que devuelven true en una función dada
def par(x): return x%2==0
lista = [1,2,3,4,5]
print(lista)
lista2 = list(filter(par, lista))
print(lista2)
