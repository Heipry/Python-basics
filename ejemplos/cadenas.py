cad = "holA, como estás?"

print(cad)
print(cad.capitalize(), "capitalize")
print(cad.lower(), "lower")
print(cad.upper(), "upper")
print(cad.swapcase(), "swapcase")
print(cad.title(), "title")
print(cad.center(50,"="))
print(cad.center(50))
print(cad.ljust(50,"="))
print(cad.rjust(50,"="))
print(cad.zfill(40))
print(cad.count('o'), 'o en la frase' )
print(cad.count('o',4), 'o en la frase después de pos4')
print(cad.find('o'),'pos de o en la frase')
print(cad.rfind('o'), 'pos de o en la frase buscando desde la derecha')
print(cad.find('o',4),'pos de o en la frase después de la 4')
print(cad.find('x'),'pos de x en la frase')
print(cad.index('o'),'index de o (index de x daría excepcion)')
print(cad.startswith('ho'),'¿empieza con ho?')
print(cad.startswith('como',6),'¿a partir de 6 es co?')
print(cad.endswith('s?'),'termina con s? ?')
print(cad.replace("o","aaa"))
cad1 = "    " + cad + "         "
print(cad1.strip(), "strip")
cad2 = "xxxx   " + cad + "         xxxxx"
print(cad2.strip('x'), "strip x")
print("_".join(cad), "join _")
parte1 = "N-0000"
parte2 = " (id=00"
parte3 = ")"
plantilla = (parte1, parte2, parte3)
print("250".join(plantilla))
print(cad.partition(" "), "partition")
print(cad.rpartition(" "), "rpartition")
print(cad.split(" "), "split")
lineas = '''hola
que
tal
estás
'''
print(lineas.splitlines(), "splitlines")