resul = False
numero=int(input("Ingrese un nro.: "))


if Par(numero) == True:
    print("Par.")
else:
    print("Impar.")



def Par(num):

    if(num%2 == 0):
        resul = True
    else:
        resul = False
    
    return resul
