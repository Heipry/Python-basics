dic1 = dict(one=1, two=2, three=3)
dic1.clear()
print(dic1, "no existe")

dict1 = {}
print(type(dict1)) 
# Crear claves sin valores
dict1 = dict.fromkeys(['a', 'b', 'c'])
print(dict1)
# Crear claves con valor genérico
dict2 = dict.fromkeys(["a","b","c"],32)
print(dict2)
# crear diccionario
dic = {"a": 2, "x": 3, "d": 4}
#unir diccionarios
dict2.update(dic)
print(dict2)
#setdefault crea el elemento si no existe, si existe no hace nada
dic.setdefault("a", 22)
dic.setdefault("e", 22)
print(dic)
#devolver elemento
print(dic.get("a"))
#extraer elemento
print(dic.pop("a"))
print(dic)
#extrar ultimo elemento
print(dic.popitem())
#lista de elementos del diccionario (como tuplas)
items = dic.items()
print(items)
#lista de claves del diccionario

keys = dic.keys()
print(keys) 
#lista de valores del diccionario

values = dic.values()
print(values)

#Estas listas se modifican dinamicamente, s iaádimso un valor al diccionario cambia el valor de la lista
dic["a"]=0
print(items)
print(keys) 
print(values)