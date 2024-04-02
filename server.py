#!/usr/bin/env python3

import socket

server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
escucha = ('localhost', 1234)
server_connection.bind(escucha)

server_connection.listen(1)

while True:
    client_socket, client_address = server_connection.accept()
    data = client_socket.recv(1024)
    
    print (f'Mensaje recibido por el cliente: {data.decode()}')
    print (f'Información del cliente que se ha conectado {client_address}')
    
    client_socket.sendall('Un saludo, crack'.encode())
    client_socket.close()