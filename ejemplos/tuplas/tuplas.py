# son como las lista pero inmutables
# Creacion
tupla1 = (1,2,3)
tupla2 = tuple([1,2,3])
tupla3 = range((3))
#empaquetado
tupla = 1,2,3
print(tupla)
#desempaquetado
a,b,c=tupla
print(a, b, c)
#operaciones
print(a in tupla)
tupla1=tupla+(4,5)
print(tupla1)
print(tupla1[4])
print(tupla1[3:5])
#No son mutables, no podemos modificar elemento o borrarlo
#metodos
print(tupla1.count(5))
print(tupla1.index(5))
