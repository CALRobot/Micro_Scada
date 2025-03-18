import tkinter as tk
from tkinter import PhotoImage
from tk_bit_led import create_bit_led, update_bit_led

def open_layout_window(parent, byte_address, main_width, main_height, background_image_path):
    """Abre la ventana de layout con las mismas dimensiones y fondo que la ventana principal."""
    layout_window = tk.Toplevel(parent)
    layout_window.title("Layout")
    layout_window.geometry(f"{main_width}x{main_height}")  # Dimensiones iguales a main

    try:
        imagen_fondo = PhotoImage(file=background_image_path)
        canvas_layout = tk.Canvas(layout_window, width=main_width, height=main_height)
        canvas_layout.create_image(0, 0, image=imagen_fondo, anchor=tk.NW)
        canvas_layout.image = imagen_fondo
        canvas_layout.pack()

        # Crear LEDs (reemplaza coordenadas y offsets)
        led1 = create_bit_led(canvas_layout, byte_address, 0, 100, 50)
        led2 = create_bit_led(canvas_layout, byte_address, 1, 200, 100)
        layout_window.leds = [led1, led2]  # Almacenar LEDs para actualización

    except tk.TclError:
        print("Error al cargar la imagen de layout.")

    volver_button = tk.Button(layout_window, text="Volver", command=layout_window.destroy)
    volver_button.pack()

    return layout_window

def update_layout_leds(layout_window, byte_address):
    """Actualiza los LEDs en la ventana de layout."""
    if hasattr(layout_window, 'leds'):
        for i, led in enumerate(layout_window.leds):
            update_bit_led(led, byte_address, i)
            