import snap7

IP = "192.168.0.1"  # Reemplaza con la IP de tu PLC
RACK = 0
SLOT = 1
DB_NUMBER = 10
BYTE_NUMBER = 56
BIT_NUMBER = 0

plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

try:
    # Leer el byte actual
    data = plc.db_read(DB_NUMBER, BYTE_NUMBER, 1)
    byte_value = data[0]

    # Modificar el bit deseado
    if BIT_NUMBER == 0:
        byte_value |= (1 << BIT_NUMBER)
    elif BIT_NUMBER == 1:
        byte_value |= (1 << BIT_NUMBER)

    # Escribir el byte modificado
    data_write = bytearray([byte_value])
    plc.db_write(DB_NUMBER, BYTE_NUMBER, data_write)
    print(f"Bit DB{DB_NUMBER}.DBX{BYTE_NUMBER}.{BIT_NUMBER} escrito a 1")

    # Leer el byte modificado
    data = plc.db_read(DB_NUMBER, BYTE_NUMBER, 1)
    bit_value = (data[0] >> BIT_NUMBER) & 1
    print(f"Valor del bit DB{DB_NUMBER}.DBX{BYTE_NUMBER}.{BIT_NUMBER}: {bit_value}")

except Exception as e:
    print(f"Error: {e}")

finally:
    plc.disconnect()