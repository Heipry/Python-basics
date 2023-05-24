minutos = input("Minutos: ")
try:
    minutos=int(minutos)
    print(minutos, "corresponde a", end=" ")
    if minutos >= 1440:
        dias=divmod(minutos, 1440)
        print(dias[0], "días", end=" ")
        minutos = dias[1]
    horas = divmod(minutos, 60)
    print(horas[0], "horas y", horas[1], "minutos")
except:
    print(minutos, "no es un número válido")


