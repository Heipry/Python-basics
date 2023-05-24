import csv
f= open("ejemplo1.csv","r")
contenido = csv.reader(f)
datos = list(contenido)
f.seek(0)

for row in datos:
    print(row)
print(datos[0])
f.close()

fichero = open("ejemplo2.csv", "w")
contenido = csv.writer(fichero)
contenido.writerow(["aaaa", 11111, "bbbbb"])
fichero.close()

