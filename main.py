
import insertar 
import actualizar
import crearProductos

crearProductos.crearBase()
activo=True

while activo:
    print("Bienvenido a la tienda Imperioyugioh")
    menu=int(input("ingrese 1-para agregar un producto 2-consultar productos  3-para actualizar 4-eliminar productos 5-mostar productos 6-reporte de bajo stock 7-salir"))
    if menu==1:
       insertar.insertar()
    elif menu==2:
        print("boton 2")
    elif menu==3:
        print("bienvenido al menu de actualizacion ingrese producto y cantidad ")
        producto=input("ingrese el producto que desee actuarlizar ")
        cantidad=int(input("ingrese la cantidad que desea actualizar " ))
        actualizar.actualizar(producto,cantidad)
    elif menu==2:
        print("boton 2")
    elif menu==7:
            activo=False
                       



