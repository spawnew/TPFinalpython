import sqlite3

def crear_tabla_personas():

     conexion = sqlite3.connect("miBaseDatos.db")

     cursor = conexion.cursor()
 
     cursor.execute('''CREATE TABLE IF NOT EXISTS Personas (

     nombre TEXT, edad INTEGER, ciudad TEXT) ''')

     conexion.commit()

     conexion.close()
def insertar():
     conexion = sqlite3.connect("miBaseDatos.db")

     cursor = conexion.cursor()
 
    # Insertar un nuevo registro en la tabla Personas

     cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Carlos',27, 'Tucumán')")
     
     
     cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES('Esteban', 32, 'Mar del Plata')")

     cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES('Valeria', 27, 'Bahía Blanca')")

     cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES('Fernando', 41, 'Rosario')")

     cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES('Carolina', 29, 'La Plata')")

     cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES('Juan', 35, 'Córdoba')")
     conexion.commit()

     conexion.close()
crear_tabla_personas()
insertar()