import socket
import sys
import os
import time

def get_date_modified(file_name):
    return os.path.getmtime(file_name)
#compares two lists and returns a list of files the server needs and a list of files the client needs
def compare_files(server_list, client_list):
    server_set = set(server_list)
    client_set = set(client_list)

    client_needs = server_set - client_set
    server_needs = client_set - server_set
    return [list(server_needs), list(client_needs)]

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

# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        #list of files in folder 
        list_of_files = [file.name for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]
        #list of times when files were modified
        list_of_time_mod = [str(get_date_modified(file.name)) for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]
        encoded_list = '/'.join(list_of_files).encode('utf-8')
        encoded_mod_list = '/'.join(list_of_time_mod).encode('utf-8')
        time.sleep(3)
        sock.sendall(encoded_list)
        sock.sendall(encoded_mod_list)
        data = sock.recv(1024)
        print('Recieved', repr(data))
            

