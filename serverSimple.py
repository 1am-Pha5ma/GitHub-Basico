import socket

IP = "0.0.0.0"
PUERTO = 5000

servidor = socket.socket()
servidor.bind((IP, PUERTO))
servidor.listen(1)

print("Esperando una conexión...")

conexion, direccion = servidor.accept()

print("Se conectó:", direccion)

while True:
    datos = conexion.recv(1024)

    if not datos:
        break

    mensaje = datos.decode("utf-8", errors="replace")
    print(mensaje)

conexion.close()
servidor.close()