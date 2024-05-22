
rango = 0
nroAnterior = 1
nroAnterior2 = 0
resultado = 0
resultados = []

rango = int(input("Ingrese tope: "))

for i in range(rango):

    resultado = nroAnterior + nroAnterior2
    resultados.append(resultado)
    nroAnterior = nroAnterior2
    nroAnterior2 = resultado

print(resultados)