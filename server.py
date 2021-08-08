import socket
import sys


#Get the host and port to be used
HOST = socket.gethostbyname(socket.gethostname())
#Using a port that is not in use
PORT = 9999

# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # server address and port number
    server_address = (HOST, PORT) 
    print("Starting up on %s port %s" % server_address)
    #bind to a port
    sock.bind(server_address)
    # begins waiting for connections
    sock.listen() 
    clientsocket, address = sock.accept()
    with clientsocket:
        print(f"Connection from {address} has been established.")
        while True:
            data = clientsocket.recv(1024)
            print(data)
            if not data:
                break
            clientsocket.sendall(data)
