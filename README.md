🛰️ Rastreador en Vivo de la Estación Espacial Internacional (ISS)

¡Observa dónde se encuentra la ISS en este momento! Este proyecto es un rastreador web dinámico que utiliza datos de la NASA y cálculo astronómico para mostrar la posición precisa de la Estación Espacial Internacional en tiempo real sobre un mapa interactivo.

✨ Características Principales

Rastreo en Tiempo Real: La posición de la ISS se actualiza automáticamente cada 5 segundos sin necesidad de recargar la página (gracias a JavaScript y una API interna de Flask).

Mapa Interactivo: Ubicación precisa marcada sobre un mapa global utilizando la librería Leaflet con un tema oscuro para una mejor inmersión espacial.

Cálculo de Iluminación: Determina si la ISS se encuentra actualmente en la cara iluminada (Día) o en la sombra de la Tierra (Noche) en esa posición.

Geolocalización: Traduce las coordenadas de latitud y longitud a una ubicación terrestre conocida (país, océano o región) utilizando la API de Geopy.

Diseño Responsivo y Estético: Interfaz moderna, con fondo de temática espacial y completamente adaptable a dispositivos móviles.

Categoría

Herramienta

Propósito

Backend

Python 3

Lógica del servidor y manejo de datos.

Framework Web

Flask

Creación del servidor web y las rutas API.

Cálculo Astronómico

pyephem

Cálculo preciso de la órbita de la ISS y el estado de iluminación.

Geocodificación

geopy

Conversión de coordenadas (Lat/Lon) a nombres de lugares legibles.

Frontend

HTML5 / Jinja2

Estructura de la página y sistema de plantillas.

Estilos

Tailwind CSS

Framework CSS de utilidad para un diseño rápido y moderno.

Interactividad

JavaScript (ES6)

Manejo de las peticiones asíncronas (fetch) y la actualización automática.

Mapas

Leaflet

Librería de mapas interactivos para visualizar la posición.

🚀 Cómo Ejecutar el Proyecto

Sigue estos pasos para poner a funcionar tu rastreador en tu máquina local.

Prerrequisitos

Necesitas tener Python 3 instalado.

1. Clonar el Repositorio

git clone [TU_URL_DEL_REPOSITORIO]
cd iss_web_tracker


2. Instalar Dependencias

Instala todas las librerías de Python necesarias (Flask, pyephem, geopy, requests):

pip install Flask pyephem geopy requests


3. Ejecutar el Servidor

Desde la carpeta principal (iss_web_tracker), inicia la aplicación Flask:

python app.py


4. Acceder a la Aplicación

Abre tu navegador web y navega a la siguiente dirección:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)


La página cargará y el marcador del satélite comenzará a moverse automáticamente.

📂 Estructura del Proyecto

iss_web_tracker/
├── app.py                  # Lógica principal del servidor Flask y rutas API.
└── templates/              # Carpeta para archivos HTML (Jinja2).
    └── index.html          # Interfaz de usuario, CSS y lógica JavaScript/Leaflet.


💡 Próximas Mejoras (Opcional)

Si deseas continuar enriqueciendo el proyecto, aquí hay algunas ideas:

[ ] Lista de Astronautas: Mostrar los nombres de las personas actualmente a bordo de la ISS.

[ ] Ruta de Órbita: Dibujar la línea de la trayectoria orbital en el mapa.

[ ] Notificaciones: Implementar un sistema para avisar al usuario cuándo la ISS pasará por encima de su ubicación.
