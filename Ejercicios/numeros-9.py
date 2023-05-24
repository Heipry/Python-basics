n1=input("Número: ")
try:
    n1 = int(n1)
    print(bin(n1)) 
except ValueError:
    print("numero no valido")