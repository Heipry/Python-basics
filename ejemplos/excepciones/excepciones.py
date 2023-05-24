a = input("Escribe un numero ")
b = 5

try:
    a = int(a)
    print(b/a)
except ValueError:
    print(a, "debe ser un numero entero")
except ZeroDivisionError as e:
    print(type(e))
    print(e.args)
    print(e, "el valor debe ser distinto de cero")
except:
    #propagar excepcion (solo util si hay un programa principal)
    raise
finally:
    print("Programa terminado")
