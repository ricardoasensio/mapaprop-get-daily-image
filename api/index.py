from flask import Flask, jsonify
import httpx
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todos los endpoints de Flask

@app.route('/daily-image', methods=['GET'])
async def get_daily_image():
    url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=es-AR'

    try:
        async with httpx.AsyncClient() as client:
            # Realizar la solicitud a la URL de Bing de forma asíncrona
            response = await client.get(url)
            response.raise_for_status()  # Levantar una excepción para errores HTTP

            # Convertir la respuesta JSON de Bing y devolverla como JSON en Flask
            data = response.json()
            image_url = f"https://www.bing.com{data['images'][0]['url']}"
            return jsonify({'imageUrl': image_url, 'data': data})

    except httpx.RequestError as e:
        # Capturar errores de solicitud (por ejemplo, conexión fallida, tiempo de espera, etc.)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
