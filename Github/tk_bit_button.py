import tkinter as tk
from plc_functions import cambiar_bit_y_led

def create_bit_frame(parent, byte_address, bit_offset):
    """
    Crea un indicador de bit con botones.

    Args:
        parent (tk.Widget): El widget padre donde se creará el indicador.
        byte_address (int): La dirección del byte del bit.
        bit_offset (int): El offset del bit dentro del byte.

    Returns:
        tk.Canvas: El objeto Canvas que representa el LED.
        tk.Button: El botón para encender el bit.
        tk.Button: El botón para apagar el bit.
    """
    bit_frame = tk.LabelFrame(parent, text=f"Byte {byte_address} Bit {bit_offset}")
    bit_frame.pack(pady=10)
    led = tk.Canvas(bit_frame, width=30, height=30)
    led.pack(side=tk.LEFT, padx=5)
    led.led = led.create_oval(5, 5, 25, 25, fill="gray")
    bit_on_button = tk.Button(bit_frame, text="Bit ON", command=lambda: cambiar_bit_y_led(10, byte_address, bit_offset, True, led))
    bit_on_button.pack(side=tk.LEFT)
    bit_off_button = tk.Button(bit_frame, text="Bit OFF", command=lambda: cambiar_bit_y_led(10, byte_address, bit_offset, False, led))
    bit_off_button.pack(side=tk.LEFT)
    return led, bit_on_button, bit_off_button

def update_bit_frame(led, state):
    """
    Actualiza el estado del LED del indicador de bit.

    Args:
        led (tk.Canvas): El objeto Canvas del LED.
        state (bool): El nuevo estado del bit (True para encendido, False para apagado).
    """
    if state:
        led.itemconfig(led.led, fill="red")
    else:
        led.itemconfig(led.led, fill="gray")