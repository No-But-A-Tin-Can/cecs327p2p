import socket
import sys
import time
import os

#compares two lists and returns a list of files the server needs and a list of files the client needs
def compare_files(server_list, client_list):
    server_set = set(server_list)
    client_set = set(client_list)

    client_needs = server_set - client_set
    server_needs = client_set - server_set
    print(type(client_needs))
    return [server_needs, client_needs]

#turns a list into a string
def list_to_string(list1):
    stringed_list = '/'.join(list1)
    return stringed_list

#turns a string into a list
def string_to_list(string1):
    listed_string = string1.split('/')
    return listed_string

#------------------------------------------

#Get the host and port to be used
HOST = socket.gethostbyname(socket.gethostname())
#Using a port that is not in use
PORT = 9999

# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    
    #list of files in folder
    list_of_files = [file.name for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]
    # server address and port number
    server_address = (HOST, PORT) 
    print("Starting up on %s port %s" % server_address)
    #bind to a port
    sock.bind(server_address)
    while True:
        # begins waiting for connections
        sock.listen() 
        clientsocket, address = sock.accept()
        with clientsocket:
            print(f"Connection from {address} has been established.")
            while True:
                #Recieve files that the client has
                data = clientsocket.recv(1024)
                data = data.decode()
                client_file_list = data.split('/')
                needed_files_list = compare_files(list_of_files, client_file_list)
                if not data:
                    break
                clientsocket.sendall(data.encode('utf-8'))
