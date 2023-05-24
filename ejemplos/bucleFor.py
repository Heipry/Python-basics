num=input("numero: ")
try:
    num=float(num)
    for i in range(11):
        #print(i,"x", num, "=", (num*i) ) #sin formato
        #print("%.2f * %.2f = %.4f" % (num, i, i*num)) #old-style
        print(f"{num:.2f} * {i:.2f} = {num*i:.4f}") #new-style
       
    else:
        print("fin")    
except:
    print(num, "no es un numero")
