import sqlite3
def actualizar(producto,cantidad):
    conexion = sqlite3.connect("miBaseDatos.db")

    cursor = conexion.cursor()
    
    
    
    
    cursor.execute("UPDATE Productos SET cantidadDisponible=? WHERE nombre=?",(cantidad,producto) )
     
     
     
    conexion.commit()
    conexion.close()