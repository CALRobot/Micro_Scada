import csv
import datetime
import os.path
import json

def generar_reportes(nombre_archivo_csv, nombre_archivo_json, valor_word40, valor_word42):
    """Genera reportes en formato CSV y JSON."""

    fecha_hora_actual = datetime.datetime.now()
    datos = {
        "fecha_hora": str(fecha_hora_actual),
        "word40": valor_word40,
        "word42": valor_word42,
    }

    generar_reporte_csv(nombre_archivo_csv, datos)
    generar_reporte_json(nombre_archivo_json, datos)

def generar_reporte_csv(nombre_archivo, datos):
    """Genera un reporte CSV, agregando líneas al archivo existente."""

    archivo_existe = os.path.isfile(nombre_archivo)

    # Formatear la marca de tiempo a HH:MM
    fecha_hora_formateada = datetime.datetime.strptime(datos["fecha_hora"], '%Y-%m-%d %H:%M:%S.%f').strftime('%H:%M')

    try:
        with open(nombre_archivo, "a", newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv, delimiter=";")
            if not archivo_existe:
                escritor_csv.writerow(["Hora", "Word 40", "Word 42"])
            escritor_csv.writerow([fecha_hora_formateada, datos["word40"], datos["word42"]])
        print(f"Reporte CSV generado con éxito: {nombre_archivo}")
    except Exception as e:
        print(f"Error al generar el reporte CSV: {e}")

def generar_reporte_json(nombre_archivo, datos):
    """Genera un reporte JSON, agregando datos al archivo existente."""

    try:
        if os.path.isfile(nombre_archivo):
            with open(nombre_archivo, "r") as archivo_json:
                try:
                    datos_existentes = json.load(archivo_json)
                except json.JSONDecodeError:
                    datos_existentes = []
        else:
            datos_existentes = []

        datos_existentes.append(datos)

        with open(nombre_archivo, "w") as archivo_json:
            json.dump(datos_existentes, archivo_json, indent=4)
        print(f"Reporte JSON generado con éxito: {nombre_archivo}")
    except Exception as e:
        print(f"Error al generar el reporte JSON: {e}")

if __name__ == '__main__':
    generar_reportes("reporte_prueba.csv", "reporte_prueba.json", 100, 200) #Para probar.