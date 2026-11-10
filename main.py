import requests
import csv

# Función que recibe una URL y un nombre de archivo de salida.
# Descarga el contenido usando requests y lo guarda localmente con codificación utf-8.
def descargarCSV(url: str, archivo_salida: str) -> None:
    try:
        # Realiza la solicitud GET a la URL proporcionada
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la solicitud no fue exitosa

        # Decodifica el contenido de la respuesta como texto
        contenido = response.text

        # Guarda el contenido en un archivo local con codificación utf-8
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)

        print(f"Archivo descargado y guardado como '{archivo_salida}'.")

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")

        # Función que recibe un año, construye el nombre del archivo CSV (ej: 'informe_ministerio_2020.csv'),
# lee la primera línea del archivo para obtener los encabezados y los devuelve en una lista.
# Debe incluir manejo de excepciones FileNotFoundError por si el archivo no fue descargado.
def recuperar_campos(anio: int) -> list:
    nombre_archivo = f"informe_ministerio_{anio}.csv"
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            encabezados = next(lector_csv)  # Lee la primera línea para obtener los encabezados
            return encabezados
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado. Asegúrese de haberlo descargado primero.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")
        return []

    # Clase EstadisticasAeropuerto
# Al instanciarse, recibe el año (int) como parámetro.
# Debe tener un método __init__ que inicialice los siguientes atributos:
# - Anio: guarda el año recibido.
# - CantModDef: se inicializa en 0 (se calculará luego).
# - AeropuertosOrigen: se inicializa como una lista vacía.
# - LineasAereas: se inicializa como una lista vacía.
class EstadisticasAeropuerto:
    def __init__(self, anio: int):
        self.Anio = anio
        self.CantModDef = 0
        self.AeropuertosOrigen = []
        self.LineasAereas = []

# Consigna 10: Graficar serie temporal con Matplotlib
# 1. Crear una lista 'anios_disponibles_x' con los años del 2020 al 2025.
# 2. Crear una lista 'lista_y' con valores simulados de promedios: [10500, 14200, 18500, 22100, 25000, 27300].
# 3. Crear una figura de tamaño (15, 6).
# 4. Generar un gráfico de barras donde el eje X son los años y el eje Y los promedios. Usar color rojo.
# 5. Agregar el título 'Promedio de movimientos por año' con tamaño de fuente 25.
# 6. Mostrar el gráfico.
import matplotlib.pyplot as plt

anios_disponibles_x = list(range(2020, 2026))
lista_y = [10500, 14200, 18500, 22100, 25000, 27300]

plt.figure(figsize=(15, 6))
plt.bar(anios_disponibles_x, lista_y, color='red')
plt.title('Promedio de movimientos por año', fontsize=25)
plt.xlabel('Año')
plt.ylabel('Promedio de movimientos')
plt.show()