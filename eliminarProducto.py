import sqlite3

def eliminarProducto():
     conexion = sqlite3.connect("miBaseDatos.db")

     cursor = conexion.cursor()
     
     producto=input("ingrese el nombre del producto a eliminar ").strip()
     
     
     cursor.execute("DELETE FROM Productos WHERE nombre=?",(producto,))
     
     conexion.commit()
     conexion.close()