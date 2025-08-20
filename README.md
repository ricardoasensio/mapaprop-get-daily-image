# MapaProp Get Daily Image

Una API REST desarrollada con Flask que proporciona acceso a la imagen diaria de Bing, específicamente configurada para el mercado argentino (es-AR). Esta API funciona como un proxy hacia el servicio Bing Image Archive, facilitando el acceso a las imágenes de alta calidad que Bing presenta diariamente en su página principal.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/ricardoasensio/mapaprop-get-daily-image)

## 🚀 Deployment Activo

Este servicio está desplegado y funcionando en:
**https://mapaprop-get-daily-image-c4qnbrmel-ricardo-asensios-projects.vercel.app**

## 🏗️ Implementación en Proyectos

Esta API está siendo utilizada en los siguientes proyectos:

- **[PucaraLabs Apps v1](https://github.com/PucaraLabs/pucaralabs-apps-v1.git)**
  - `mapaprop-v2`: Implementación principal del sistema MapaProp
  - `memudoya-app`: Aplicación del proyecto Memudoya

## 👨‍💻 Autor

Desarrollado por **Ricardo Asensio** ([ricardoasensio](https://github.com/ricardoasensio))

## Características

- 🌅 Obtiene automáticamente la imagen diaria de Bing
- 🇦🇷 Configurado para el mercado argentino (es-AR)
- ⚡ Respuestas rápidas con httpx asíncrono
- 🌐 CORS habilitado para uso desde navegadores
- 🚀 Desplegable en Vercel con Serverless Functions
- 🛡️ Manejo robusto de errores y excepciones

## API Endpoints

### GET /daily-image

Obtiene la imagen diaria de Bing junto con sus metadatos.

**Respuesta exitosa (200):**
```json
{
  "imageUrl": "https://www.bing.com/th?id=OHR.BirdMigration_ES-AR8829372624_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp",
  "data": {
    "images": [
      {
        "startdate": "20250820",
        "fullstartdate": "202508200700",
        "enddate": "20250821",
        "url": "/th?id=OHR.BirdMigration_ES-AR8829372624_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp",
        "urlbase": "/th?id=OHR.BirdMigration_ES-AR8829372624",
        "copyright": "Bandada de grullas comunes en vuelo, Alemania (© Sandra Kühnapfel/Getty Images)",
        "copyrightlink": "https://www.bing.com/search?q=grullas+comunes&form=hpcapt",
        "title": "Un espectáculo aéreo natural",
        "quiz": "/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20250820_BirdMigration%22",
        "wp": true,
        "hsh": "8a9c7b2d1e3f4g5h6i7j8k9l0m1n2o3p",
        "drk": 1,
        "top": 1,
        "bot": 1,
        "hs": []
      }
    ]
  }
}
```

**Respuesta de error (500):**
```json
{
  "error": "Connection timeout"
}
```

### Campos de respuesta

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `imageUrl` | string | URL completa de la imagen de alta resolución |
| `data` | object | Datos completos devueltos por la API de Bing |
| `data.images[0].copyright` | string | Información de copyright de la imagen |
| `data.images[0].title` | string | Título descriptivo de la imagen |
| `data.images[0].startdate` | string | Fecha de inicio (formato YYYYMMDD) |
| `data.images[0].copyrightlink` | string | Enlace para más información sobre la imagen |

## Ejemplo de uso

### JavaScript (Fetch API)
```javascript
fetch('https://mapaprop-get-daily-image-c4qnbrmel-ricardo-asensios-projects.vercel.app/daily-image')
  .then(response => response.json())
  .then(data => {
    console.log('Imagen diaria:', data.imageUrl);
    console.log('Título:', data.data.images[0].title);
    console.log('Copyright:', data.data.images[0].copyright);
  })
  .catch(error => console.error('Error:', error));
```

### cURL
```bash
curl https://mapaprop-get-daily-image-c4qnbrmel-ricardo-asensios-projects.vercel.app/daily-image
```

### Python
```python
import requests

response = requests.get('https://mapaprop-get-daily-image-c4qnbrmel-ricardo-asensios-projects.vercel.app/daily-image')
data = response.json()

print(f"Imagen: {data['imageUrl']}")
print(f"Título: {data['data']['images'][0]['title']}")
```

## Estructura del proyecto

```
mapaprop-get-daily-image/
├── api/
│   └── index.py          # Aplicación Flask principal
├── package.json          # Configuración Node.js (v22.x)
├── requirements.txt      # Dependencias Python
├── vercel.json          # Configuración de deployment
└── README.md           # Documentación
```

## Dependencias

### Python
- **Flask 3.0.3**: Framework web ligero y flexible
- **flask-cors 4.0.1**: Extensión para habilitar CORS
- **httpx 0.27.0**: Cliente HTTP asíncrono de alto rendimiento
- **Flask[async] 3.0.3**: Soporte para funciones asíncronas en Flask

### Runtime
- **Node.js 22.x**: Entorno de ejecución para el deployment en Vercel

## Desarrollo local

### Prerrequisitos
- Python 3.8+
- Node.js 22.x
- Vercel CLI

### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/ricardoasensio/mapaprop-get-daily-image.git
cd mapaprop-get-daily-image
```

2. Instala las dependencias de Python:
```bash
pip install -r requirements.txt
```

3. Instala Vercel CLI globalmente:
```bash
npm i -g vercel
```

### Ejecutar localmente

```bash
vercel dev
```

La aplicación estará disponible en `http://localhost:3000`.

### Probar el endpoint

```bash
curl http://localhost:3000/daily-image
```

## Deployment en Vercel

### Deployment automático

Conecta tu repositorio a Vercel para deployments automáticos en cada push.

### Deployment manual

```bash
vercel --prod
```

### Variables de entorno

Este proyecto no requiere variables de entorno adicionales para funcionar.

## Configuración

### Cambiar mercado geográfico

Para cambiar el mercado de la imagen (actualmente configurado para Argentina), modifica la URL en `api/index.py`:

```python
# Mercado argentino (actual)
url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=es-AR'

# Otros mercados disponibles:
# España: mkt=es-ES
# México: mkt=es-MX
# Estados Unidos: mkt=en-US
# Reino Unido: mkt=en-GB
```

### Personalizar respuesta

Puedes modificar el formato de respuesta editando la función `get_daily_image()` en `api/index.py`.

## Limitaciones

- La API depende de la disponibilidad del servicio Bing Image Archive
- Las imágenes están sujetas a los derechos de autor de Microsoft/Bing
- El servicio está optimizado para el mercado argentino por defecto

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añade nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Créditos

- Imágenes proporcionadas por Microsoft Bing
- Desarrollado para uso en proyectos MapaProp
