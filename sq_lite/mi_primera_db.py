#importando modulo
import sqlite3
# crear conexion a la base de datos 
conn=sqlite3.connect("instituo.db")
# Crear tabla de carreras
# conn.execute(
#     """
#     CREATE TABLE CARRERAS
#     (id INTEGER PRIMARY KEY,
#     nombre TEXT NOT NULL,
#     duracion INTEGER NOT NULL);
#     """
# )
## se define con may el tipo de variable y la variable, sintaxis de la tabla
# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Ingeniería en Informática', 5)
    """
)
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Administración', 4)
    """
)


# Consultar datos
print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS") #seleciona todo de la tabla de carreras
for row in cursor:
    print(row)
#CARRERAS:
#(1, 'Ingeniería en Informática', 5)
#(2, 'Licenciatura en Administración', 4)

# Crear tablas de estudiantes
conn.execute(
    """
    CREATE TABLE ESTUDIANTES
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL);
    """
)
# Insertar datos de estudiantes
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('Juan', 'Perez', '2000-05-15') 
    """
)   ## expresamos una cadena dentro de una cadena con comillas simples
# en las fechas se sigue un formato , similar a mandar parametros como en poo
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('María', 'Lopez', '1999-08-20')
    """
)

# Consultar datos de estudiantes
print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)
    
# ESTUDIANTES:
# (1, 'Juan', 'Perez', '2000-05-15')
# (2, 'María', 'Lopez', '1999-08-20')

# Crear tabla de matriculación
conn.execute(
    """
    CREATE TABLE MATRICULACION
    (id INTEGER PRIMARY KEY,
    estudiante_id INTEGER NOT NULL,
    carrera_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
) 
#llaves foraneas de otras tablas  
# foreign key .... refe.. lo que hace es verificar si existe para insertarlo

### vamos a matricular un estudiante
# Insertar datos de matriculación
conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (1, 1, '2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (2, 2, '2024-01-20')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)
# Consultar datos de matriculación
print("\nMATRICULACION:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha 
    FROM MATRICULACION
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)
# MATRICULACION:
# ('Juan', 'Perez', 'Ingeniería en Informática', '2024-01-15')
# ('María', 'Lopez', 'Licenciatura en Administración', '2024-01-20')
# ('Juan', 'Perez', 'Licenciatura en Administración', '2024-01-25')    




# Eliminar una fila de la tabla de matriculación
# vamos actualizar una matriculacion anterior menet era 20 de enero 
# tener en cuenta WHERE  identificar su funcion
conn.execute(
    """
    DELETE FROM MATRICULACION
    WHERE id = 3
    """
)

# Listar datos de matriculación
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)
for row in cursor:
    print(row)
    
# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-20')

# Actualizar una fila de la tabla de matriculación
conn.execute(
    """
    UPDATE MATRICULACION
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)
# Listar datos de matriculación
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)
for row in cursor:
    print(row)
    
# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-30')

# Cerrar conexión
conn.close()