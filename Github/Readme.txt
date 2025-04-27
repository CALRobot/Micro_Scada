Micro Scada - Comunicación S7-1500 con Python

Descripción:

Esta aplicación Python permite la comunicación con un PLC Siemens S7-1500 simulado con PLC SIM Advanced a través de la librería python-snap7. 
La interfaz gráfica, creada con Tkinter, permite leer y escribir Words y Bits en el PLC.

Requisitos:

* TIA Portal 17 con PLC SIM Advanced (maquina VmWare)
* PLC Siemens S7-1500 (simulado)
* Python 3.x  Uso el IDE Thonny Python 4.1.4, que lleva todo excepto este paquete:
* python-snap7 2.0.2
* Thonny IDE (opcional)

Instalación:

1.  Asegúrese de tener TIA Portal 17 y PLC SIM Advanced instalados y configurados.
2.  Instale Python 3.x y la librería python-snap7 2.0.2.
3.  Clone este repositorio.
4.  Abra el archivo main.py con Thonny o su editor de Python preferido.
5.  Asegúrese de que la dirección IP del PLC en el código coincide con la dirección IP de su PLC virtual.
6.  Ejecute main.py.

Uso:

* La interfaz muestra los valores de Word1 y Word2, y permite escribir nuevos valores.
* También muestra el estado de los Bits del Byte 50 y permite activarlos o desactivarlos individualmente, o el byte completo.
* Existe un clock visual con un led que parpadea a 500ms.
* Los botones "Borrar" y "Salir" realizan las funciones correspondientes.

Notas:

* Esta aplicación ha sido probada en un entorno virtualizado con VMware.
* La version de python-snap7 2.0.2 ha sido copiada manualmente en el entorno virtual.

Contacto:

[ Carlos Alberto Lara de GitHub ]
[ laracarlosalberto@ymail.com ]
[ calingrobot@gmail.com ]

Puntos claves:

    Conciso y directo al grano.
    Lista clara de requisitos.
    Instrucciones de instalación sencillas.
    Descripción breve de la interfaz y su uso.
    Notas importantes sobre el entorno de prueba.
    Informacion de contacto.

Este README.txt proporcionará a los usuarios una visión general rápida de tu proyecto y cómo utilizarlo.
