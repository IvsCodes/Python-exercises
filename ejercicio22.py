#Pide al usuario el número de un mes (1 al 12) y escribe su nombre en pantalla. 
#Utilizar la sentencia for


meses = ["","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
eleccion = int(input("Elija un nro. del 1 al 12: "))


for i in meses[eleccion]:
    print(i)
