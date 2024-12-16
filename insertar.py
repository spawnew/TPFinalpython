import sqlite3
def insertar():
     conexion = sqlite3.connect("miBaseDatos.db")

     cursor = conexion.cursor()
     nombre=input("nombre para agregar a la base de dato ").strip().lower()
     descripcion=input("descripcion para agregar a la base de dato ").strip().lower()
     cantidad=int(input("cantidad disponible para agregar a la base de dato "))
     precio=int(input("precio para agregar a la base de dato "))
     categoria=input("categoria para agregar a la base de dato ").strip().lower()
   
   
   
   
   
    # Insertar un nuevo registro en la tabla Productos

     cursor.execute("INSERT INTO Productos (nombre,descripcion,cantidadDisponible,precio,categoria ) VALUES (?,?,?,?,?)",(nombre,descripcion,cantidad,precio,categoria))
     
     
     
     conexion.commit()
     conexion.close()