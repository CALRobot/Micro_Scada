import tkinter as tk
from plc_functions import cambiar_bit_y_led

def create_bit_frame(parent, byte_address, bit_offset):
    bit_frame = tk.LabelFrame(parent, text=f"Byte {byte_address} Bit {bit_offset}")
    bit_frame.pack(pady=10)
    led = tk.Canvas(bit_frame, width=30, height=30)
    led.pack(side=tk.LEFT, padx=5)
    led.led = led.create_oval(5, 5, 25, 25, fill="gray")
    bit_on_button = tk.Button(bit_frame, text="Bit ON", command=lambda: cambiar_bit_y_led(10, byte_address, bit_offset, True, led))
    bit_on_button.pack(side=tk.LEFT)
    bit_off_button = tk.Button(bit_frame, text="Bit OFF", command=lambda: cambiar_bit_y_led(10, byte_address, bit_offset, False, led))
    bit_off_button.pack(side=tk.LEFT)
    return led
	