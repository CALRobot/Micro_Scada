import tkinter as tk
from plc_functions import escribir_byte

def create_byte_frame(parent, byte_address):
    byte_frame = tk.LabelFrame(parent, text=f"Byte {byte_address}")
    byte_frame.pack(pady=10)
    byte_on_button = tk.Button(byte_frame, text="Byte ON", command=lambda: escribir_byte(10, byte_address, 0xFF))
    byte_on_button.pack(side=tk.LEFT)
    byte_off_button = tk.Button(byte_frame, text="Byte OFF", command=lambda: escribir_byte(10, byte_address, 0x00))
    byte_off_button.pack(side=tk.LEFT)
	