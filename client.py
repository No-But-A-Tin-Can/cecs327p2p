import socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(b'Hello, world!')
    data = sock.recv(1024)
            
print('Recieved', repr(data))
