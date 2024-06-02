# Desarrolle un algoritmo que permita determinar a partir de un número de días, 
# ingresado por pantalla, ¿Cuántos años, meses, semanas y días; constituyen el número 
# de días proporcionado utilizando la estructura While.

nroDias = input("Ingrese la cantidad de días: ")


print(int(nroDias) / 365, "año/s")
print(int(nroDias) / 30, "mes/es")
print(int(nroDias) / 7, "semana/s")