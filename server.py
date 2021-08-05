import socket
import sys

# Creation of a TCP/IP socket

#Get the host and port to be used
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # AF_INET = IPv4 SOCK_STREAM = TCP
    server_address = (HOST, PORT) # server address and port number
    print("Starting up on %s port %s" % server_address)
    sock.bind(server_address)
    sock.listen() # begins waiting for connections
    clientsocket, address = sock.accept()
    with clientsocket:
        print(f"Connection from {address} has been established.")
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            conn.sendall(data)
