
import sqlite3

def listarCompleto():
     conexion = sqlite3.connect("miBaseDatos.db")

     cursor = conexion.cursor()
     
     cursor.execute("SELECT * FROM Productos ")
     resultado=cursor.fetchall()
     for producto in resultado:
         print("Nombre:",producto[0],
               "Descripcion",producto[1],
               "CantidadDisponible:",producto[2],
               "Precio:",producto[3] ,
                "Categoria:",producto[4]
               )
    
     
     conexion.commit()
     conexion.close()