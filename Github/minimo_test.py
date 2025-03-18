"""

Lamento que el error persista. Vamos a realizar una revisión más exhaustiva para asegurarnos de que estamos cancelando los after correctamente.

1. Revisar la función parpadear_led:

    Asegúrate de que la función parpadear_led esté configurando parpadeo_id correctamente cada vez que se llama a ventana.after().
    Revisa si hay alguna lógica condicional que pueda estar impidiendo que se asigne un nuevo parpadeo_id.

2. Revisar la función actualizar_estado:

    Similarmente, verifica que actualizar_estado esté configurando actualizar_id correctamente.

3. Asegurarse de que salir() se llama correctamente:

    Verifica que la función salir() se esté llamando correctamente cuando cierras la ventana principal.
    Coloca un print("salir() called") al principio de la función salir() para confirmar que se está ejecutando.

4. Crear un ejemplo mínimo reproducible:

    Si el problema persiste, intenta crear un ejemplo mínimo reproducible que demuestre el error.
    Esto implica eliminar todo el código innecesario y dejar solo las partes relevantes para reproducir el error.
    Un ejemplo mínimo reproducible facilitará la identificación y solución del problema.

5. Revisar el orden de los afters:

    Asegurarse de que no haya ningun after que llame a otro after.
    Si fuera el caso, asegurarse de cancelar el after padre, antes de cancelar el hijo.

Ejemplo de cómo crear un ejemplo mínimo reproducible:

"""


import tkinter as tk

ventana = tk.Tk()

parpadeo_id = None
actualizar_id = None

def parpadear_led():
    global parpadeo_id
    print("parpadear_led")
    parpadeo_id = ventana.after(250, parpadear_led)

def actualizar_estado():
    global actualizar_id
    print("actualizar_estado")
    actualizar_id = ventana.after(500, actualizar_estado)

def salir():
    global parpadeo_id, actualizar_id
    if parpadeo_id:
        ventana.after_cancel(parpadeo_id)
    if actualizar_id:
        ventana.after_cancel(actualizar_id)
    ventana.destroy()

parpadear_led()
actualizar_estado()

ventana.protocol("WM_DELETE_WINDOW", salir)

ventana.mainloop()