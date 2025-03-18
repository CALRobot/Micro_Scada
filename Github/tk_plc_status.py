import tkinter as tk
import snap7
import datetime

def create_plc_status_frame(parent, plc):
    """
    Crea un Frame para mostrar el estado del PLC y la fecha/hora.

    Args:
        parent (tk.Widget): El widget padre donde se creará el Frame.
        plc (snap7.client.Client): El objeto cliente de snap7.

    Returns:
        tk.Frame: El Frame con la información del estado del PLC y la fecha/hora.
    """
    status_frame = tk.LabelFrame(parent, text="Estado del PLC")
    status_frame.pack(pady=10)

    status_label = tk.Label(status_frame, text="Estado: Desconectado")
    status_label.pack()
    status_frame.status_label = status_label

    datetime_label = tk.Label(status_frame, text="")
    datetime_label.pack()
    status_frame.datetime_label = datetime_label

    status_frame.plc = plc

    return status_frame

def update_plc_status_frame(status_frame):
    """
    Actualiza la información del estado del PLC y la fecha/hora.

    Args:
        status_frame (tk.Frame): El Frame que contiene la información del estado del PLC.
    """
    try:
        cpu_state = status_frame.plc.get_cpu_state().lower() # Convertir a minúsculas
        if "run" in cpu_state: # Comparación más robusta
            status_frame.status_label.config(text="Estado: En RUN", fg="green")
        else:
            status_frame.status_label.config(text="Estado: Detenido", fg="red")
    except Exception:
        status_frame.status_label.config(text="Estado: Desconectado", fg="gray")

    now = datetime.datetime.now()
    status_frame.datetime_label.config(text=now.strftime("%Y-%m-%d %H:%M:%S"), font=("Helvetica", 12, "bold"))