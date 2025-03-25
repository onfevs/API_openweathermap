# API_openweathermap

"""
# Análisis Climático con OpenWeatherMap

Este repositorio contiene un script en Python que consume la API de OpenWeatherMap para obtener datos climáticos de puntos aleatorios alrededor de un lugar central (en este caso, Muzo, Colombia). Los datos obtenidos incluyen información como la temperatura, humedad, presión, velocidad del viento, descripción del clima, entre otros.

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
Configuración
1. Obtén tu API Key de OpenWeatherMap
Para utilizar la API de OpenWeatherMap, necesitas una clave de API. Si aún no tienes una, puedes obtenerla registrándote en el sitio web de OpenWeatherMap.

Una vez que tengas tu clave, reemplázala en el código en la variable api_key.

python
Mostrar siempre los detalles

Copiar
api_key = "TU_API_KEY_AQUI"
2. Configuración de las coordenadas
El script está configurado para generar puntos aleatorios alrededor de las coordenadas de Muzo, Colombia (latitud: 5.067680, longitud: -75.509819). Si deseas cambiar el lugar central, solo tienes que modificar las variables central_lat y central_lon.

python
Mostrar siempre los detalles

Copiar
central_lat = 5.067680  # Latitud de Muzo
central_lon = -75.509819  # Longitud de Muzo
3. Rango de puntos aleatorios
El script genera puntos aleatorios dentro de un radio de 10 kilómetros alrededor del lugar central. Puedes cambiar este valor modificando la variable radius_km.

python
Mostrar siempre los detalles

Copiar
radius_km = 10  # Radio en kilómetros
4. Generación de puntos
El script genera 50 puntos aleatorios y obtiene datos climáticos y de elevación de cada uno de estos puntos.

python
Mostrar siempre los detalles

Copiar
random_points = generate_random_points_around_central_point(50, central_lat, central_lon, radius_km)
5. Guardado de los datos
Los datos generados se guardan en formato GeoJSON en el archivo especificado por la variable output_file.

python
Mostrar siempre los detalles

Copiar
output_file = "ruta/del/archivo.geojson"
Cómo usar el script
Clona este repositorio en tu máquina local:

bash
Mostrar siempre los detalles

Copiar
git clone https://github.com/tu_usuario/analisis-climatico.git
Accede al directorio del repositorio:

bash
Mostrar siempre los detalles

Copiar
cd analisis-climatico
Ejecuta el script en Python:

bash
Mostrar siempre los detalles

Copiar
python analizar_clima.py
Los datos se guardarán en un archivo GeoJSON en la ruta especificada en output_file.

Estructura de los Datos
El archivo generado es un archivo GeoJSON que contiene los datos climáticos y de elevación de cada uno de los puntos aleatorios generados. La estructura de los datos en el archivo será similar a la siguiente:

json
Mostrar siempre los detalles

Copiar
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
Cada punto contiene información de latitud, longitud, temperatura, humedad, presión atmosférica, entre otros.

Contribuciones
Si deseas contribuir al proyecto, por favor crea un fork del repositorio y envía un pull request con tus cambios.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles. """
