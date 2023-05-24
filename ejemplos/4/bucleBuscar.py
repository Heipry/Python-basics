frase = input("Escribe una frase: ")
for elem in frase:
    if elem == "a": 
        print("a existe en la frase")
        exit()
print("La letra a no aparece en la frase")
