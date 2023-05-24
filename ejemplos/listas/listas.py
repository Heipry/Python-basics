
# crear lista
lista1 =[]
lista2 = list()
lista3 = list("palabra")
print(list(enumerate(lista3)))
lista4 = list(range(1,6))
print("-------")
# operaciones con elementos
lista = [1,2,3,4,5]
print(type(lista[1]))
for i in lista:
    print(i)
print(3 in lista)
print(3 not in lista)
print(lista+[6,7,8,9])
print(lista * 3)
print(lista[0])
lista[2] = 0
print(lista)
lista[3:4] = [0,0]
print(lista)
del lista[2:5]
print(lista)
lista = lista*2
print(lista)
print(id(lista))
print("-------")
#slice
print(lista[2:4])
print(lista[2:])
print(lista[:4])
print(lista[2:5:2])
print(lista[::-1])
print("-------")
# funciones (no modifican lista)
print(lista)
print(type(lista))
print(len(lista))
print(max(lista))
print(min(lista))
print(sum(lista))
print(sorted(lista))
print(sorted(lista, reverse=True))
print("-------")
# copiar lista
lista1 = lista[:]
print(lista)
print(id(lista))
print(lista1)
print(id(lista1))
lista2 =lista.copy() 
# tablas
tabla =[lista, lista1, [1,2,3,4]]
print("tabla:")
for fila in tabla:
    for elem in fila:
        print(elem, end=" ")
    print("")
#metodos (modifican lista)
lista.append(2)   
print("-------")
print(lista)
lista.extend([100,101])   
print(lista)
lista.insert(4, "new")   
print(lista)
lista.remove("new")  
print(lista)
lista.sort()    
print(lista)
lista.sort(reverse=True)    
print(lista, "sort")
lista.sort(key=int.bit_length)    
print(lista)
lista.pop( )     
print(lista)
lista.reverse()
print(lista)
lista.clear()  
print(lista)
# metodos de consulta
print(lista1.count(5))    
print(lista1.index(2))   

