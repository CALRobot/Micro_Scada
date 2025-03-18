import tkinter as tk

def create_vumetro_frame(parent, title, width, height, max_valor):
    vumetro_frame = tk.LabelFrame(parent, text=title)
    vumetro_frame.pack(pady=10)

    vumetro = tk.Canvas(vumetro_frame, width=width, height=height, bg="white")
    vumetro.rect = vumetro.create_rectangle(0, height, width, height, fill="green")
    vumetro.width = width
    vumetro.height = height
    vumetro.pack()

    vumetro.max_valor = max_valor  # Guardar el valor máximo

    return vumetro

def actualizar_vumetro_frame(vumetro, valor, title):
    nivel = int((valor / vumetro.max_valor) * vumetro.height)
    vumetro.coords(vumetro.rect, 0, vumetro.height - nivel, vumetro.width, vumetro.height)
    vumetro.master.config(text=f"{title}: {valor}")  # Actualizar el título
    