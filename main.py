import sqlite3
import sqlite3

def conectar():
    conexion = sqlite3.connect("test.db")
    return conexion

def cargar_materias():
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = "SELECT id,nombre from materias;"
        cur.execute(sql)
        resultado = cur.fetchall()
        print(resultado)
        resultado2 = []
        for r in resultado:
            resultado2.append({"id": r[0], "nombre": r[1]})
        return resultado2
    finally:
        cone.close()

print(cargar_materias())