import sqlite3
def consultaProducto():
    

     conexion = sqlite3.connect("miBaseDatos.db")

     cursor = conexion.cursor()
     producto=input("ingrese el producto a buscar ").strip().lower()
     
     cursor.execute("SELECT * FROM Productos WHERE nombre=?", (producto,))
     resultado=cursor.fetchall()
     for producto in resultado:
         print("Nombre:",producto[0],
               "CantidadDisponible:",producto[2],
               "PRECIO:",producto[3] 
               )
    
     
     conexion.commit()
     conexion.close()