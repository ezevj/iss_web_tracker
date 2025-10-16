from flask import Flask, render_template, jsonify
import requests
import ephem
from geopy.geocoders import Nominatim
import ssl


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context




def obtener_posicion_iss():
    """Obtiene la latitud y longitud actual de la ISS desde la API."""
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json", timeout=5)
        response.raise_for_status()
        datos = response.json()
        latitud = datos['iss_position']['latitude']
        longitud = datos['iss_position']['longitude']
        return float(latitud), float(longitud)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la posición de la ISS: {e}")
        return None, None

def obtener_nombre_lugar(latitud, longitud):
    """Convierte coordenadas en un nombre de lugar usando Geopy y Nominatim."""
    try:
       
        geolocator = Nominatim(user_agent="rastreador_iss_v2_final_project")
        
        
        location = geolocator.reverse(f"{latitud}, {longitud}", language='es', timeout=10)
        
       
        return location.address if location else "Sobre el océano o zona remota."
        
    except Exception as e:
        print(f"Error al obtener el nombre del lugar: {e}")
        return "No se pudo determinar el lugar (Error de geocodificación)."

def estado_iluminacion_iss(latitud, longitud):
    """
    Usa PyEphem para determinar si la ISS está sobre una zona de día o noche.
    """
    try:
        
        obs = ephem.Observer()
        obs.lat = str(latitud)
        obs.lon = str(longitud)
        
      
        sol = ephem.Sun()
        sol.compute(obs)

       
        altitud_grados = ephem.degrees(sol.alt)
        
        if altitud_grados > 0:
            return "De Día (Iluminada)"
        else:
            return "De Noche (Sombra)"

    except Exception as e:
        print(f"Error en el cálculo de iluminación con PyEphem: {e}")
        return "Estado Desconocido"



app = Flask(__name__)


@app.route('/')
def index():
    
    lat, lon = obtener_posicion_iss()

    if lat is not None and lon is not None:
        
        nombre_lugar = obtener_nombre_lugar(lat, lon)
        estado = estado_iluminacion_iss(lat, lon)

       
        return render_template('index.html',
                               latitud=f"{lat:.4f}", 
                               longitud=f"{lon:.4f}",
                               lugar=nombre_lugar,
                               iluminacion=estado)
    else:
        return "<h1>Error de Conexión</h1><p>No se pudo obtener la posición de la ISS.</p>"


@app.route('/data')
def get_iss_data():
    lat, lon = obtener_posicion_iss()
    
    if lat is not None and lon is not None:
        
        nombre_lugar = obtener_nombre_lugar(lat, lon)
        estado = estado_iluminacion_iss(lat, lon)

        
        return jsonify({
            'latitud': f"{lat:.4f}",
            'longitud': f"{lon:.4f}",
            'lugar': nombre_lugar,
            'iluminacion': estado
        })
    else:
        
        return jsonify({'error': 'No data available'}), 500



if __name__ == '__main__':
    app.run(debug=True)
