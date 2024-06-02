contador = 0
totalNros = 0
bandera = True
media = 0

while bandera:

    nro = int(input("Ingrese un número para mediar o 0 para finalizar: "))
    
    if nro == 0:
        bandera = False
    else:
        totalNros += totalNros + nro
        contador += 1

print("La media total es de",float(totalNros / contador))