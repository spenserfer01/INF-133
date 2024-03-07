import requests

# Definir la consulta GraphQL
query = """
    {
        estudiante{
        
            id
            nombre
            apellido
            carrera
        }
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)


### queris mutacion y subscripciones
#es posibleagregar campos de parametros