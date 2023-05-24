#devuelve numero de dias del mes introducido
mes = input("Número de mes: ")
try:
    mes = int(mes)
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    nombre_meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    if mes>len(meses) or mes<1:
        raise Exception()   
    print("El mes", mes, "es", nombre_meses[mes-1], "y tiene", meses[mes-1], "días")
except:
    print(mes, "no es un mes válido")
