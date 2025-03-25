import random
import requests
import json
import math

# Tu API Key de OpenWeather
api_key = "TU API"

# Coordenadas exactas de Muzo, Colombia (Latitud y Longitud) y un rango para generar puntos aleatorios
central_lat = 5.067680  # Latitud del punto central 
central_lon = -75.509819  # Longitud del punto central 
radius_km = 10  # Radio en kilómetros para la generación de puntos aleatorios alrededor del punto central

# Función para obtener todos los datos climáticos en un punto específico
def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if 'main' in data:
        # Guardar todos los datos importantes (temperatura, humedad, presión, etc.)
        weather_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]  # Lon primero, luego lat para ArcGIS
            },
            "properties": {
                "temperature": data['main']['temp'],  # Temperatura en grados Celsius
                "humidity": data['main']['humidity'],  # Humedad relativa (%)
                "pressure": data['main']['pressure'],  # Presión atmosférica (hPa)
                "temp_min": data['main']['temp_min'],  # Temperatura mínima
                "temp_max": data['main']['temp_max'],  # Temperatura máxima
                "feels_like": data['main']['feels_like'],  # Temperatura que se siente (o "sensación térmica")
                "weather_description": data['weather'][0]['description'],  # Descripción del clima (nublado, soleado, etc.)
                "wind_speed": data['wind']['speed'],  # Velocidad del viento (m/s)
                "wind_deg": data['wind']['deg'],  # Dirección del viento (grados)
                "clouds": data['clouds']['all'],  # Porcentaje de nubes en el cielo
                "visibility": data.get('visibility', 'N/A')  # Visibilidad en metros (si está disponible)
            }
        }
        return weather_data
    return None

# Función para obtener la elevación de un punto usando la API Open Elevation
def get_elevation(lat, lon):
    elevation_url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
    elevation_response = requests.get(elevation_url)
    elevation_data = elevation_response.json()
    
    if 'results' in elevation_data:
        return elevation_data['results'][0]['elevation']  # Elevación en metros
    return None

# Función para calcular la nueva latitud y longitud dentro de un radio alrededor de un punto
def generate_random_point_within_radius(lat, lon, radius_km):
    # Convertir el radio de kilómetros a grados de latitud y longitud
    radius_deg_lat = radius_km / 111  # Aproximadamente 1 grado de latitud = 111 km
    radius_deg_lon = radius_km / (111 * math.cos(math.radians(lat)))  # Ajuste para longitud según la latitud
    
    # Generar un punto aleatorio dentro del radio
    random_lat = lat + random.uniform(-radius_deg_lat, radius_deg_lat)
    random_lon = lon + random.uniform(-radius_deg_lon, radius_deg_lon)
    
    return random_lat, random_lon

# Generar puntos aleatorios alrededor del punto central
def generate_random_points_around_central_point(n, lat, lon, radius_km):
    points = []
    random.seed()  # Asegura que cada ejecución genere puntos diferentes
    for _ in range(n):
        random_lat, random_lon = generate_random_point_within_radius(lat, lon, radius_km)
        
        # Obtener datos climáticos y elevación
        weather_data = get_weather_data(random_lat, random_lon)
        elevation = get_elevation(random_lat, random_lon)
        
        if weather_data and elevation is not None:
            point_data = {
                "latitude": random_lat,
                "longitude": random_lon,
                "elevation": elevation,
                **weather_data["properties"]  # Desempaqueta los datos climáticos en el punto
            }
            points.append(point_data)
    
    return points

# Generar 60 puntos aleatorios alrededor del punto de Muzo
random_points = generate_random_points_around_central_point(50, central_lat, central_lon, radius_km)

# Crear la estructura final para el archivo JSON
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [point["longitude"], point["latitude"]]  # Lon primero, luego lat para ArcGIS
            },
            "properties": {
                "temperature": point["temperature"],
                "humidity": point["humidity"],
                "pressure": point["pressure"],
                "temp_min": point["temp_min"],
                "temp_max": point["temp_max"],
                "feels_like": point["feels_like"],
                "weather_description": point["weather_description"],
                "wind_speed": point["wind_speed"],
                "wind_deg": point["wind_deg"],
                "clouds": point["clouds"],
                "visibility": point["visibility"],
                "elevation": point["elevation"]
            }
        } for point in random_points
    ]
}

# Especificar la ruta donde deseas guardar el archivo JSON
output_file = "TU RUTA PARA GUARDAR EL GEOJSON"

# Guardar los puntos con toda la información climática y de elevación en un archivo JSON
with open(output_file, 'w') as json_file:
    json.dump(geojson_data, json_file, indent=4)

print(f"Datos guardados en {output_file}")
