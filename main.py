
import insertar 
import actualizar
import crearProductos
import eliminarProducto
import listarCompleto
import reporteBajoStock
import consultaProducto
crearProductos.crearBase()
activo=True

while activo:
    print("Bienvenido a la tienda Imperioyugioh")
    menu=int(input(""" Ingrese al menu:
                   1-para agregar un producto
                   2-consultar productos 
                   3-para actualizar
                   4-eliminar productos 
                   5-mostar productos 
                   6-reporte de bajo stock 
                   7-salir """))
   #triple comillas para concatena texto 
    if menu==1:
       insertar.insertar()
    elif menu==2:
        consultaProducto.consultaProducto()
    elif menu==3:
        print("bienvenido al menu de actualizacion ingrese producto y cantidad ")
        producto=input("ingrese el producto que desee actuarlizar ")
        cantidad=int(input("ingrese la cantidad que desea actualizar " ))
        actualizar.actualizar(producto,cantidad)
    elif menu==4:
        eliminarProducto. eliminarProducto()
    elif menu==5:
        listarCompleto.listarCompleto()
    elif menu==6:
        reporteBajoStock. reporteBajoStock()
    elif menu==7:
            activo=False
                       



