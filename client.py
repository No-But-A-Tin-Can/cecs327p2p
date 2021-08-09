import socket
import sys
import time
import os

#turns a list into a string
def list_to_string(list1):
    stringed_list = '/'.join(list1)
    return stringed_list

#turns a string into a list
def string_to_list(string1):
    listed_string = string1.split('/')
    return listed_string

#-----------------------------------------

#Get the host and port to be used
HOST = socket.gethostbyname(socket.gethostname())
#Using a port that is not in use
PORT = 9999

encoded_list = '/'.join(list_of_files).encode('utf-8')
#[item.encode('utf-8') for item in list_of_files]
print(encoded_list)

# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #list of files in folder 
    list_of_files = [file.name for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]
    sock.connect((HOST, PORT))
    while True:
        time.sleep(2)
        sock.sendall(encoded_list)
        data = sock.recv(1024)
        print('Recieved', repr(data))
            

