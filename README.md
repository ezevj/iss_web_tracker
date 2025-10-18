# 🛰️ Rastreador en Vivo de la Estación Espacial Internacional (ISS)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"/>
</p>

¡Observa dónde se encuentra la ISS en este momento! Este proyecto es un rastreador web dinámico que utiliza datos de la NASA y cálculo astronómico para mostrar la posición precisa de la Estación Espacial Internacional en tiempo real sobre un mapa interactivo.

---

## 🎥 Demostración del Proyecto


---

## ✨ Características Principales

* **🛰️ Rastreo en Tiempo Real**: La posición de la ISS se actualiza automáticamente cada 5 segundos sin recargar la página.
* **🗺️ Mapa Interactivo**: Ubicación precisa sobre un mapa global de Leaflet con un tema oscuro para una mejor inmersión.
* **☀️/🌙 Cálculo de Iluminación**: Determina si la ISS está de día o de noche según su posición.
* **📍 Geolocalización**: Traduce las coordenadas a una ubicación terrestre conocida (país, océano, etc.).
* **📱 Diseño Responsivo**: Interfaz moderna y adaptable a cualquier dispositivo, móvil o de escritorio.

---

## 🛠️ Tecnologías Utilizadas

| Categoría  | Tecnología      | Propósito                                                      |
| :--------- | :-------------- | :------------------------------------------------------------- |
| **Backend** | Python 3        | Lógica del servidor y manejo de datos.                         |
|            | Flask           | Creación del servidor web y las rutas API.                     |
|            | pyephem         | Cálculo preciso de la órbita y el estado de iluminación.       |
|            | geopy           | Conversión de coordenadas (Lat/Lon) a nombres de lugares.      |
| **Frontend** | HTML5 / Jinja2  | Estructura de la página y sistema de plantillas.               |
|            | Tailwind CSS    | Framework CSS para un diseño rápido y moderno.                 |
|            | JavaScript (ES6)| Manejo de peticiones asíncronas (fetch) y actualización.        |
|            | Leaflet         | Librería de mapas interactivos para visualizar la posición.    |

---

## 🚀 Cómo Ejecutar el Proyecto

Sigue estos pasos para poner a funcionar el rastreador en tu máquina local.

#### Prerrequisitos
* Necesitas tener **Python 3** instalado.

#### 1. Clonar el Repositorio
```bash
git clone [TU_URL_DEL_REPOSITORIO]
cd iss_web_tracker
```

#### 2. Instalar Dependencias
```bash
pip install Flask pyephem geopy requests

```
#### 3. Ejecutar el Servidor
```bash
python app.py
```

4. Acceder a la Aplicación
Abre tu navegador y ve a: http://127.0.0.1:5000/


## 📂 Estructura del Proyecto
```
iss_web_tracker/
├── app.py # Lógica principal del servidor Flask y rutas API. 
└── templates/ 
└── index.html # Interfaz, CSS y lógica JavaScript/Leaflet.
```
