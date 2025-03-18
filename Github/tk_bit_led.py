import tkinter as tk
from plc_functions import leer_bit

def create_bit_led(parent, byte_address, bit_offset, x, y):
    """
    Crea un LED que muestra el estado de un bit del PLC en coordenadas específicas.

    Args:
        parent (tk.Widget): El widget padre donde se creará el LED.
        byte_address (int): La dirección del byte del bit.
        bit_offset (int): El offset del bit dentro del byte.
        x (int): Coordenada x del LED.
        y (int): Coordenada y del LED.

    Returns:
        tk.Canvas: El objeto Canvas que representa el LED.
    """
    
    """
    # LED DE 5MM
    led = tk.Canvas(parent, width=30, height=30, highlightthickness=0)
    led.place(x=x, y=y)
    led.led = led.create_oval(5, 5, 25, 25, fill="gray")
    return led
    """

    # LED DE 3MM
    led = tk.Canvas(parent, width=20, height=20, highlightthickness=0)  # Tamaño reducido a 20x20
    led.place(x=x, y=y)
    led.led = led.create_oval(3, 3, 17, 17, fill="gray")  # Óvalo más pequeño
    return led

def update_bit_led(led, byte_address, bit_offset):
    """
    Actualiza el estado del LED en función del estado del bit del PLC.

    Args:
        led (tk.Canvas): El objeto Canvas del LED.
        byte_address (int): La dirección del byte del bit.
        bit_offset (int): El offset del bit dentro del byte.
    """
    state = leer_bit(10, byte_address, bit_offset)
    if state is not None:
        if state:
            led.itemconfig(led.led, fill="red")
        else:
            led.itemconfig(led.led, fill="gray")
            