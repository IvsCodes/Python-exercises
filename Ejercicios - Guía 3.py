numero = input("Ingrese un número: ")
numero = float(numero)

if numero == 0:
    print("Es cero.")
elif numero > 0:
    print("Es positivo.")
else:
    print("Es negativo.")




numero_entero = int(input("Ingrese un número entero: "))

if numero_entero % 2 == 0:
    print("Es par.")
else: 
    print("Es impar.")



numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro: "))
numero3 = float(input("Y otro más: "))

if numero1 >= numero2 and numero1 >= numero3:
    print("El mayor es "+str(numero1)+".")
elif numero2 >= numero3 and numero2 >= numero1:
    print("El mayor es "+str(numero2)+".")
elif numero3 >= numero1 and numero3 >= numero2:
    print("El mayor es "+str(numero3)+".")
else:
    print("Ingresó un caracter.")


nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda: "))
nota3 = float(input("Ingrese la tercera: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 6:
    print("¡Aprobado!")
else:
    print("Desaprobado.")