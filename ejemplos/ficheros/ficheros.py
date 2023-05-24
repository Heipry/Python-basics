f= open("ejemplo.txt","w")
print(f.closed)
print(f.mode)
print(f.name)
f.write(
    "Texto de prueba\n"
)
f.write("Texto de prueba2\n")
f.close()
with open("ejemplo.txt") as archivo:
    contenido = archivo.read()
print(contenido)

f= open("ejemplo.txt","r")
print(f.readline())
print(f.readline())
print(".",f.readline(),".")
f.seek(0)
print(f.readlines())