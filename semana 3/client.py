import requests

# Definir la consulta GraphQL
query = """
    {
        Bye Bye
        Hello, world!
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query}) #mandas al Resqauest un url con un jeison que es un diccionario
print(response.text)