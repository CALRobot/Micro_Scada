import snap7
from tkinter import messagebox
import time

# Configuración del PLC
IP = "192.168.0.1"
RACK = 0
SLOT = 1
DB_NUMBER = 10

# Instancia única del cliente Snap7
plc = snap7.client.Client()

def conectar_plc():
    try:
        plc.connect(IP, RACK, SLOT)
        print("Conexión PLC establecida.")
    except Exception as e:
        print(f"Error detallado al conectar al PLC: {e}")
        messagebox.showerror("Error", f"Error al conectar al PLC: {e}")
        exit()

def desconectar_plc():
    if plc.get_connected():
        plc.disconnect()
        print("Conexión PLC cerrada.")

# Esta cambia un bit que SI esta asociado a un led canvas
def cambiar_bit_y_led(db_num, start_byte, boolean_index, bool_value, led_canvas):
    try:
        data_read = plc.db_read(db_num, start_byte, 1)
        byte_value = data_read[0]
        if bool_value:
            byte_value |= (1 << boolean_index)
            led_canvas.itemconfig(led_canvas.led, fill="red")
        else:
            byte_value &= ~(1 << boolean_index)
            led_canvas.itemconfig(led_canvas.led, fill="gray")
        data_write = bytearray([byte_value])
        plc.db_write(db_num, start_byte, data_write)
    except Exception as e:
        messagebox.showerror("Error", f"Error al scrivere bits: {e}")
        
# Esta cambia un bit que NO esta asociado a un led canvas
def cambiar_bit(db_num, start_byte, boolean_index, bool_value):
    try:
        data_read = plc.db_read(db_num, start_byte, 1)
        byte_value = data_read[0]
        if bool_value:
            byte_value |= (1 << boolean_index)
        else:
            byte_value &= ~(1 << boolean_index)
        data_write = bytearray([byte_value])
        plc.db_write(db_num, start_byte, data_write)
    except Exception as e:
        messagebox.showerror("Error", f"Error al scrivere bits: {e}")


def leer_bit(db_num, start_byte, boolean_index):
    try:
        data_read = plc.db_read(db_num, start_byte, 1)
        byte_value = data_read[0]
        bit_value = (byte_value >> boolean_index) & 1
        return bool(bit_value)
    except Exception as e:
        messagebox.showerror("Error", f"Error al leggere bit: {e}")
        return None

def escribir_word(word_address, entry, resultado_label):
    try:
        word_valor = int(entry.get())
        word_data = word_valor.to_bytes(2, byteorder="big")
        plc.db_write(DB_NUMBER, word_address, word_data)
        messagebox.showinfo("Éxito", f"Dato scritto correttamente (Word {word_address})")
    except Exception as e:
        messagebox.showerror("Error", f"Error al scrivere dati (Word {word_address}): {e}")


def leer_word(word_address, resultado_label):
    max_tentativi = 3
    tentativo = 0
    while tentativo < max_tentativi:
        try:
            word_data = plc.db_read(DB_NUMBER, word_address, 2)
            word_valor = int.from_bytes(word_data, byteorder="big")
            resultado_label.config(text=f"Valor Word: {word_valor}", fg="blue")  # Valor en azul
            return
        except Exception as e:
            print(f"Tentativo {tentativo + 1} fallito: {e}")
            tentativo += 1
            time.sleep(1)
    resultado_label.config(text=f"Valor Word: Error", fg="red") # Error en rojo
    messagebox.showerror("Error", f"Impossibile leggere dati (Word {word_address}) dopo {max_tentativi} tentativi.")

def escribir_byte(db_num, start_byte, byte_value):
    try:
        data_write = bytearray([byte_value])
        plc.db_write(db_num, start_byte, data_write)
    except Exception as e:
        messagebox.showerror("Error", f"Error al scrivere byte: {e}")
        