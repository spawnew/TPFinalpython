import sqlite3

def reporteBajoStock():
     conexion = sqlite3.connect("miBaseDatos.db")

     cursor = conexion.cursor()
     
     cursor.execute("SELECT * FROM Productos WHERE CantidadDisponible <10")
     resultado=cursor.fetchall()
     for producto in resultado:
         print("Nombre:",producto[0],
               "CantidadDisponible:",producto[2],
               "PRECIO:",producto[3] 
               )
    
     
     conexion.commit()
     conexion.close()