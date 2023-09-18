import requests

# URL del endpoint que deseas probar
url = "http://localhost:8000/predict"  # Asegúrate de usar la URL correcta
data = {
    "flights": [
        {
            "OPERA": "Aerolineas Argentinas", 
            "TIPOVUELO": "N", 
            "MES": 3
        }
    ]
}
response = requests.post(url, json=data)

# Verifica la respuesta
if response.status_code == 200:
    print("Respuesta exitosa:")
    print(response.text)
else:
    print("La solicitud falló con el código de estado:", response.status_code)