# tk_alarma_warning.py
import tkinter as tk
from tkinter import scrolledtext
from plc_functions import cambiar_bit  # Importa cambiar_bit
from tkinter import messagebox

MARCA_CONFIRMAR_ALARMA = (10, 56, 0) #DB10.DBX56.0
MARCA_RESET_ALARMA = (10, 56, 1) #DB10.DBX56.1

alarma_confirmada = False # Variable de estado

def inicializar_cuadro_texto(ventana):
    """Crea e inicializa el cuadro de texto para alarmas y warnings."""
    cuadro_texto = scrolledtext.ScrolledText(ventana, height=4, wrap=tk.WORD, state=tk.DISABLED)
    cuadro_texto.grid(row=1, column=0, columnspan=4, sticky="ew", padx=10, pady=10)
    ventana.grid_rowconfigure(1, weight=1)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)
    ventana.grid_columnconfigure(3, weight=1)

    return cuadro_texto

def mostrar_mensaje(cuadro_texto, texto, tipo):
    """Muestra un mensaje en el cuadro de texto con el color correspondiente."""
    cuadro_texto.config(state=tk.NORMAL)
    if tipo == "alarma":
        cuadro_texto.tag_config("rojo", foreground="red")
        cuadro_texto.insert(tk.END, texto + "\n", "rojo")
    elif tipo == "warning":
        cuadro_texto.tag_config("azul", foreground="blue")
        cuadro_texto.insert(tk.END, texto + "\n", "azul")
    cuadro_texto.config(state=tk.DISABLED)

def confirmar_alarma(ventana): #ventana añadida como argumento
    """Confirma la alarma."""
    global alarma_confirmada
    cambiar_bit(MARCA_CONFIRMAR_ALARMA[0], MARCA_CONFIRMAR_ALARMA[1], MARCA_CONFIRMAR_ALARMA[2], True)
    ventana.after(1000, lambda: cambiar_bit(MARCA_CONFIRMAR_ALARMA[0], MARCA_CONFIRMAR_ALARMA[1], MARCA_CONFIRMAR_ALARMA[2], False)) #Genera pulso
    alarma_confirmada = True

def resetear_alarmas(cuadro_texto, ventana): #ventana añadida como argumento
    """Resetea las alarmas y limpia el cuadro de texto."""
    global alarma_confirmada
    if alarma_confirmada:
        cambiar_bit(MARCA_RESET_ALARMA[0], MARCA_RESET_ALARMA[1], MARCA_RESET_ALARMA[2], True)
        ventana.after(1000, lambda: cambiar_bit(MARCA_RESET_ALARMA[0], MARCA_RESET_ALARMA[1], MARCA_RESET_ALARMA[2], False)) #Genera pulso
        cuadro_texto.config(state=tk.NORMAL)
        cuadro_texto.delete(1.0, tk.END)
        cuadro_texto.config(state=tk.DISABLED)
        alarma_confirmada = False
    else:
        messagebox.showinfo("Información", "Por favor, confirme la alarma primero.")

def crear_botones_confirmar_reset(ventana, cuadro_texto):
    """Crea los botones de confirmar y reset de alarmas."""
    confirmar_button = tk.Button(ventana, text="Confirmar Alarma", command=lambda: confirmar_alarma(ventana)) #ventana pasada como argumento
    confirmar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    reset_button = tk.Button(ventana, text="Reset Alarmas", command=lambda: resetear_alarmas(cuadro_texto, ventana)) #ventana pasada como argumento
    reset_button.grid(row=2, column=2, columnspan=2, padx=10, pady=5, sticky="ew")

    return confirmar_button, reset_button