listaProductos=["Tomate","Lechuga","Papa",]
listaPrecios=[10,5,3]
listaStock=[20,10,25]
cajaAbierta=True
respuesta=""
productoVendido=""
cantidadVendida=0
facturacionTotal=0
ventas=0
ticket=0
cierre=True
validacionExistencia=True
index=0



def validacion_numerica(var):
    while not var.isnumeric():
        print("Error, solo debe contener números.")
        var=input()
    return int(var)

def validacion_alfa(var):
    while not var.isalpha():
        print("Error, solo debe contener letras.")
        var=input()
    return var  



while cajaAbierta:

    while cierre:
        print("Tenemos papa, lechuga y tomate. \n ¿Qué desea comprar?")
        
        while validacionExistencia:
            productoVendido=input()
            productoVendido=validacion_alfa(productoVendido)
            productoVendido=productoVendido.capitalize()

            

            for i in listaProductos:
                if i == productoVendido:
                    index=listaProductos.index(productoVendido)     #Función de List que devuelve el índice de la primer coincidencia en la lista
                    print("¿Cuánto desea comprar?")
                    cantidadVendida=input()
                    validacion_numerica(cantidadVendida)
                    cantidadVendida=validacion_numerica(cantidadVendida)
                    if cantidadVendida > listaStock[index] or cantidadVendida == 0:
                        print("No tenemos stock.")
                        
                    else:
                        listaStock[index]=listaStock[index] - cantidadVendida
                        ventas=ventas+1
                        ticket=ticket+listaPrecios[index]*cantidadVendida
                        facturacionTotal=facturacionTotal+ticket

            if index == 0:    ## si el  producto no se encontró el índice seguirá en cero
                    print("Error, el producto no existe.")

             
       
            if ticket>0:       ## chequeo de ticket mayor a cero para que no se imprima en consola si el ticket está vacío
                print("El ticket actual es de $"+str(ticket))

            respuesta=input("¿Desea continuar? S o N: ")
            respuesta=respuesta.upper()
            if respuesta == "N":
                cajaAbierta=False
                cierre=False
            elif respuesta == "S":
                cajaAbierta=True
                cierre=True
            else:
                print("Error, intente nuevamente: ")
                respuesta=input("¿Desea continuar? S o N: ")
                respuesta=respuesta.upper()



print("Caja cerrada.")                      
print("Cantidad de ventas: "+str(ventas))
print("Facturación total: ",facturacionTotal)
print("Ticket promedio: "+str(ticket/ventas))
