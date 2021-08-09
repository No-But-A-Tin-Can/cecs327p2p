import socket
import sys
import time
import os
import pickle

#Get the host and port to be used
HOST = socket.gethostbyname(socket.gethostname())
#Using a port that is not in use
PORT = 9999

#list of files in the directory at the start of the 
list_of_files = [file.name for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]
encoded_list = '/'.join(list_of_files).encode('utf-8')
#[item.encode('utf-8') for item in list_of_files]
print(encoded_list)

# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        time.sleep(2)
        sock.sendall(encoded_list)
        data = sock.recv(1024)
        print('Recieved', repr(data))
            

