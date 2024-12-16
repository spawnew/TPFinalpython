import sqlite3
def crearBase():

     conexion = sqlite3.connect("miBaseDatos.db")

     cursor = conexion.cursor()
 
     cursor.execute('''CREATE TABLE IF NOT EXISTS Productos (

     nombre TEXT,descripcion TEXT, cantidadDisponible INTEGER, precio INTEGER,categoria TEXT) ''')

     conexion.commit()

     conexion.close()