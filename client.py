import socket
import sys
import time
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        time.sleep(2)
        sock.sendall(b'Test message')
        data = sock.recv(1024)
        print('Recieved', repr(data))
            

