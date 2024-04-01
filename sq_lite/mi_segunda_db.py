import sqlite3
# crear conexion a la base de datos 
conn=sqlite3.connect("instituo.db")
# Crear tabla de carreras
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL);
    """
)
## se define con may el tipo de variable y la variable, sintaxis de la tabla
# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio,categoria) 
    VALUES ('pasta', 5,1)
    """
)



# Consultar datos
print("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS") #seleciona todo de la tabla de carreras
for row in cursor:
    print(row)
