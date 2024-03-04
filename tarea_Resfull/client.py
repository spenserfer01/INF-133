import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"

# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.get(ruta_get)
print("Todos los estudiantes:")
print(get_response.json())

# GET obtener todas las carreras por la ruta /carreras
ruta_carreras = url + "carreras"
get_carreras_response = requests.get(ruta_carreras)
print("\nTodas las carreras:")
print(get_carreras_response.json())

# GET obtener a todos los estudiantes de la carrera de "Economía"
ruta_estudiantes_economia = url + "estudiantes/carrera/Economía"
get_estudiantes_economia_response = requests.get(ruta_estudiantes_economia)
print("\nEstudiantes de Economía:")
print(get_estudiantes_economia_response.json())

# POST agregar un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.post(ruta_post, json=nuevo_estudiante)
print("\nNuevo estudiante agregado:")
print(post_response.json())

# POST agregar otro nuevo estudiante por la ruta /estudiantes
nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingeniería",
}
post_response = requests.post(ruta_post, json=nuevo_estudiante)
print("\nNuevo estudiante agregado:")
print(post_response.json())

# GET buscar a un estudiante por id /estudiantes/{id}
ruta_filtrar_nombre = url + "estudiantes/1"
filtrar_nombre_response = requests.get(ruta_filtrar_nombre)
print("\nEstudiante con ID 1:")
print(filtrar_nombre_response.json())

# PUT actualizar un estudiante por la ruta /estudiantes
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
put_response = requests.put(ruta_post, json=estudiante_actualizado)
print("\nEstudiante actualizado:")
print(put_response.json())

# DELETE eliminar todos los estudiantes por la ruta /estudiantes
eliminar_response = requests.delete(ruta_get)
print("\nEstudiantes eliminados:")
print(eliminar_response.json())
