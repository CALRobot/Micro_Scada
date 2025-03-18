"""
import tkinter as tk
from plc_functions import leer_word, escribir_word

def create_word_frame(parent, word_address):
    word_frame = tk.LabelFrame(parent, text=f"Word: Byte {str(word_address)}-{str(word_address + 1)}")  # Conversión a cadena
    word_frame.pack(pady=10)
    word_entry = tk.Entry(word_frame)
    word_entry.pack()
    word_label = tk.Label(word_frame, text="Valor Word: ")
    word_label.pack()
    word_leer_button = tk.Button(word_frame, text="Leer Word", command=lambda: leer_word(word_address, word_label))
    word_leer_button.pack(side=tk.LEFT)
    word_escribir_button = tk.Button(word_frame, text="Escribir Word", command=lambda: escribir_word(word_address, word_entry, word_label))
    word_escribir_button.pack(side=tk.LEFT)
    return word_entry, word_label
"""

import tkinter as tk
from plc_functions import leer_word, escribir_word

def create_word_frame(parent, word_address):
    word_frame = tk.LabelFrame(parent, text=f"Word: Byte {str(word_address)}-{str(word_address + 1)}")
    word_frame.pack(pady=10)
    word_entry = tk.Entry(word_frame)
    word_entry.pack()
    word_label = tk.Label(word_frame, text="Valor Word: ", font=("Helvetica", 12, "bold")) # Fuente en negrita
    word_label.pack()
    word_leer_button = tk.Button(word_frame, text="Leer Word", command=lambda: leer_word(word_address, word_label))
    word_leer_button.pack(side=tk.LEFT)
    word_escribir_button = tk.Button(word_frame, text="Escribir Word", command=lambda: escribir_word(word_address, word_entry, word_label))
    word_escribir_button.pack(side=tk.LEFT)
    return word_entry, word_label
