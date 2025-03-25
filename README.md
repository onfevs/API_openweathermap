# Análisis Climático con OpenWeatherMap

Este repositorio contiene un script en Python que consume la API de OpenWeatherMap para obtener datos climáticos de puntos aleatorios alrededor de un lugar central (en este caso, Colombia). Los datos obtenidos incluyen información como la temperatura, humedad, presión, velocidad del viento, descripción del clima, entre otros.

https://openweathermap.org/

## Requisitos

- Python 3.x
- Paquetes:
  - `requests`
  - `json`
  - `math`
  - `random`

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install requests

```

##  Configuración
# 1. Obtén tu API Key de OpenWeatherMap
Para utilizar la API de OpenWeatherMap, necesitas una clave de API. Si aún no tienes una, puedes obtenerla registrándote en el sitio web de OpenWeatherMap.

Una vez que tengas tu clave, reemplázala en el código en la variable api_key.
```
api_key = "TU_API_KEY_AQUI"
```
# 2. Configuración de las coordenadas
El script está configurado para generar puntos aleatorios alrededor de las coordenadas de Muzo, Colombia (latitud: 5.067680, longitud: -75.509819). Si deseas cambiar el lugar central, solo tienes que modificar las variables central_lat y central_lon.
```
central_lat = 5.067680  # Latitud 
central_lon = -75.509819  # Longitud 
```

Link : https://www.latlong.net/

# 3. Rango de puntos aleatorios
El script genera puntos aleatorios dentro de un radio de 10 kilómetros alrededor del lugar central. Puedes cambiar este valor modificando la variable radius_km.
```
radius_km = 10  # Radio en kilómetros
```
# 4. Generación de puntos
El script genera 50 puntos aleatorios y obtiene datos climáticos y de elevación de cada uno de estos puntos.
```
random_points = generate_random_points_around_central_point(50, central_lat, central_lon, radius_km)
```
# 5. Guardado de los datos
Los datos generados se guardan en formato GeoJSON en el archivo especificado por la variable output_file.
```
output_file = "ruta/del/archivo.geojson"
```
## Estructura de los Datos
El archivo generado es un archivo GeoJSON que contiene los datos climáticos y de elevación de cada uno de los puntos aleatorios generados. La estructura de los datos en el archivo será similar a la siguiente:
```
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-75.510000, 5.067000]
            },
            "properties": {
                "temperature": 22.5,
                "humidity": 80,
                "pressure": 1012,
                "temp_min": 20,
                "temp_max": 25,
                "feels_like": 22,
                "weather_description": "clear sky",
                "wind_speed": 3.0,
                "wind_deg": 180,
                "clouds": 0,
                "visibility": 10000,
                "elevation": 600
            }
        },
        ...
    ]
}
```
Cada punto contiene información de latitud, longitud, temperatura, humedad, presión atmosférica, entre otros.

## Contribuciones
Si deseas contribuir al proyecto, por favor crea un fork del repositorio y envía un pull request con tus cambios.

