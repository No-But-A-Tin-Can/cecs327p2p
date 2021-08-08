import socket
import sys
import time
import os

#Get the host and port to be used

HOST = socket.gethostbyname(socket.gethostname())
#Using a port that is not in use
PORT = 9999

#list of files in the directory at the start of the 
list_of_files = [file.name for file in os.scandir() if file.is_file()]
print(list_of_files)

# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        time.sleep(2)
        sock.sendall(b'Test message')
        data = sock.recv(1024)
        print('Recieved', repr(data))
            

