import socket
import sys

class Client:

    def __init__(self):
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 9999

        # AF_INET = IPv4 SOCK_STREAM = TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            s.sendall(b'Hello, world!')
            data = s.recv(1024)
            full_msg = ''
            
        print('Recieved', repr(data))
