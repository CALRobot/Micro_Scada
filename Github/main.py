import tkinter as tk
from tkinter import PhotoImage
from plc_functions import conectar_plc, desconectar_plc, leer_bit, leer_word, escribir_byte, plc
from tk_word import create_word_frame
from tk_bit import create_bit_frame
from tk_byte import create_byte_frame
from tk_clock import create_clock_frame
from tk_vumetro import create_vumetro_frame, actualizar_vumetro_frame
from tk_plc_status import create_plc_status_frame, update_plc_status_frame
from tk_bit_led import create_bit_led, update_bit_led
from layout_window import open_layout_window, update_layout_leds
from tk_report import generar_reportes #Importamos tk_report
import schedule
import time
import threading
import datetime #Importamos datetime
import tk_alarma_warning  # Importa tk_alarma_warning.py


# Cuadro de texto para alarmas y warnings (inicia var global)
cuadro_texto = None


# Configurazione degli indirizzi
WORD1_ADDRESS = 40
WORD2_ADDRESS = 42
BYTE_ADDRESS = 50

# IDs delle chiamate after()
actualizar_id = None
parpadeo_id = None

# Vumetri
vumetro1 = None
vumetro2 = None

# Frame di stato PLC
plc_status_frame = None

def actualizar_estado():
    global actualizar_id
    try:
        # Aggiorna Words
        leer_word(WORD1_ADDRESS, word1_label)
        leer_word(WORD2_ADDRESS, word2_label)

        # Aggiorna Vumetri
        actualizar_vumetro_frame(vumetro1, int(word1_label.cget("text").split(": ")[1]), f"Word {WORD1_ADDRESS}")
        actualizar_vumetro_frame(vumetro2, int(word2_label.cget("text").split(": ")[1]), f"Word {WORD2_ADDRESS}")

        # Aggiorna LED dei bit
        for i in range(8):
            bit_estado = leer_bit(10, BYTE_ADDRESS, i)
            if bit_estado is not None:
                leds[i].itemconfig(leds[i].led, fill="red" if bit_estado else "gray")

        # Aggiorna stato PLC
        update_plc_status_frame(plc_status_frame)

        # Aggiorna LED in layout_window
        if hasattr(ventana, 'layout_window') and ventana.layout_window.winfo_exists():
            update_layout_leds(ventana.layout_window, BYTE_ADDRESS)

        actualizar_id = ventana.after(500, actualizar_estado)
    except Exception as e:
        print(f"Error en actualizar_estado: {e}")

def borrar_entradas():
    word1_entry.delete(0, tk.END)
    word2_entry.delete(0, tk.END)

"""
Error al cerrar aplicacion:
El error que estás recibiendo indica que las funciones: 'actualizar_estado' y 'parpadear_led',
están intentando ejecutarse después de que la ventana principale di Tkinter ha sido destruida.
Esto se debe a que las llamadas a 'ventana.after()' que programan la ejecución periódica de estas funciones
no se están cancelando correctamente antes de que la ventana se cierre.
"""

def salir():
    global actualizar_id, parpadeo_id
    desconectar_plc()
    if actualizar_id:
        ventana.after_cancel(actualizar_id)
    if parpadeo_id:
        ventana.after_cancel(parpadeo_id)
    ventana.destroy()

def byte_on():
    escribir_byte(10, BYTE_ADDRESS, 0xFF)

def byte_off():
    escribir_byte(10, BYTE_ADDRESS, 0x00)

# Configurazione della finestra principale
# Configuración de la ventana principal
ventana = tk.Tk()
ventana.resizable(False, False)
ventana.title("Micro Scada Siemens - V1.0.0 ")
ventana.geometry("800x850")

# Carica immagine di sfondo
try:
    imagen_fondo = PhotoImage(file="fondo6.png")
    label_fondo = tk.Label(ventana, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    label_fondo.image = imagen_fondo
except tk.TclError:
    print("Errore: Impossibile caricare l'immagine di sfondo.")

# Colonna 1: Words
words_frame = tk.Frame(ventana)
words_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
word1_entry, word1_label = create_word_frame(words_frame, WORD1_ADDRESS)
word2_entry, word2_label = create_word_frame(words_frame, WORD2_ADDRESS)

# Vumetri
vumetro1 = create_vumetro_frame(words_frame, f"Word {WORD1_ADDRESS}", 20, 100, 32767)
vumetro2 = create_vumetro_frame(words_frame, f"Word {WORD2_ADDRESS}", 20, 100, 32767)

# Colonna 2: Bits
bits_frame = tk.Frame(ventana)
bits_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")
bit1_frame = tk.LabelFrame(bits_frame, text="Bits Byte 50")
bit1_frame.pack(pady=10)
leds = [create_bit_frame(bit1_frame, BYTE_ADDRESS, i) for i in range(8)]
byte_on_button = tk.Button(bits_frame, text="Byte ON", command=byte_on)
byte_on_button.pack(pady=5)
byte_off_button = tk.Button(bits_frame, text="Byte OFF", command=byte_off)
byte_off_button.pack(pady=5)

# Colonna 3: Generale
general_frame = tk.Frame(ventana)
general_frame.grid(row=0, column=2, padx=10, pady=10, sticky="n")


"""
# Colonna 4: Report
report_frame = tk.Frame(ventana)
report_frame.grid(row=0, column=3, padx=10, pady=10, sticky="n")

# Bottone Crear Reporte
def crear_reporte():
    nombre_archivo = f"reporte_{datetime.date.today()}.csv"
    valor_word40 = int(word1_label.cget("text").split(": ")[1])
    valor_word42 = int(word2_label.cget("text").split(": ")[1])
    generar_reporte_diario(nombre_archivo, valor_word40, valor_word42)

reporte_button = tk.Button(report_frame, text="Crear Reporte", command=crear_reporte)
reporte_button.pack()


''''''''''''''''

'''''''''''''''
"""

# Colonna 4: Report
report_frame = tk.Frame(ventana)
report_frame.grid(row=0, column=3, padx=10, pady=10, sticky="n")

# Bottone Crear Reporte
def crear_reporte():
    nombre_archivo_csv = f"reporte_{datetime.date.today()}.csv"
    nombre_archivo_json = f"reporte_{datetime.date.today()}.json"
    valor_word40 = int(word1_label.cget("text").split(": ")[1])
    valor_word42 = int(word2_label.cget("text").split(": ")[1])
    generar_reportes(nombre_archivo_csv, nombre_archivo_json, valor_word40, valor_word42)

reporte_button = tk.Button(report_frame, text="Crear Reporte", command=crear_reporte)
reporte_button.pack()



# Stato PLC
conectar_plc()
plc_status_frame = create_plc_status_frame(general_frame, plc)
plc_status_frame.pack()


# Bottone Layout
def abrir_layout():
    # Se agrega el if para no abrir dos ventanas iguales
    if not hasattr(ventana, 'layout_window') or not ventana.layout_window.winfo_exists():
        ventana.layout_window = open_layout_window(ventana, BYTE_ADDRESS, ventana.winfo_width(), ventana.winfo_height(), "fondo6.png")
        ventana.layout_window.transient(ventana)

layout_button = tk.Button(general_frame, text="Layout", command=abrir_layout)
layout_button.pack()


led_clock = create_clock_frame(general_frame)
borrar_button = tk.Button(general_frame, text="Cancella", command=borrar_entradas)
borrar_button.pack(pady=5)
salir_button = tk.Button(general_frame, text="Esci", command=salir)
salir_button.pack(pady=5)

led_color = "gray"
def parpadear_led():
    global led_color, parpadeo_id
    if led_color == "gray":
        led_color = "yellow"
    else:
        led_color = "gray"
    led_clock.itemconfig(led_clock.led, fill=led_color)
    parpadeo_id = ventana.after(250, parpadear_led)

parpadear_led()

# Aggiorna lo stato
actualizar_estado()

# Generazione report automatica
def generar_reporte_turno():
    """Genera un reporte al final de cada turno."""
    nombre_archivo = f"reporte_{datetime.date.today()}.csv"
    generar_reporte_diario(nombre_archivo)

# Programar la generación del reporte al final de cada turno
schedule.every().day.at("06:00").do(generar_reporte_turno)
schedule.every().day.at("14:00").do(generar_reporte_turno)
schedule.every().day.at("22:00").do(generar_reporte_turno)

# Ejecutar el scheduler en un hilo separado
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
        
thread = threading.Thread(target=run_scheduler)
thread.daemon = True # Permitir que el hilo termine cuando la aplicación termina
thread.start()

# Cuadro de texto para alarmas y warnings
cuadro_texto = tk_alarma_warning.inicializar_cuadro_texto(ventana)

# Botones de confirmar y reset de alarmas (pulsos al PLC)
tk_alarma_warning.crear_botones_confirmar_reset(ventana, cuadro_texto)


# ... (resto del código)

# Ejemplo de uso
tk_alarma_warning.mostrar_mensaje(cuadro_texto, "Alarma de temperatura alta", "alarma")
tk_alarma_warning.mostrar_mensaje(cuadro_texto, "Warning: nivel de combustible bajo", "warning")

# Botones de confirmar y reset de alarmas (pulsos al PLC)
tk_alarma_warning.crear_botones_confirmar_reset(ventana, cuadro_texto)

ventana.mainloop()
