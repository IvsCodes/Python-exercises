
legajo = 0
horasTrabajadas = 0
excedente = 0
salario = 0
valorUnitarioDeHora = 0
bandera = True
respuesta = ""
maximo = 0
totalSalarios = 0
salarioMaximo = 0
empleadoConSalarioMaximo = 0
promedioGeneral = 0


while bandera == True:
    legajo = int(input("Ingrese su nro. de legajo: "))

    horasTrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

    valorUnitarioDeHora = int(input("Ingrese el valor por hora: "))


    if valorUnitarioDeHora <= 40:
        
        salario = horasTrabajadas * valorUnitarioDeHora
        excedente = (horasTrabajadas - 40) * valorUnitarioDeHora * 1,5 + (40 * valorUnitarioDeHora)
        totalSalarios = salario + totalSalarios + excedente

    else:
        salario = horasTrabajadas * valorUnitarioDeHora
        totalSalarios = totalSalarios + salario
    
    if salario > maximo:
        maximo = salario
        empleadoConSalarioMaximo = legajo

    respuesta = input(("¿Desea continuar? S o N: ")).upper()

    if respuesta == "N":
        bandera = False

print("El salario máximo es de ", maximo, " y corresponde al legajo ", empleadoConSalarioMaximo,".")
print("El total de salarios pagados es de ", totalSalarios,".")