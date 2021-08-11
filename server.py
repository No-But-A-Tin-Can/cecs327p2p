import socket
import sys
import os
import time

#gets date a file was modified
def get_date_modified(file_name):
    return os.path.getmtime(file_name)

#compares two lists and returns a list of files the server needs and a list of files the client needs
def compare_files(server_list, client_list, server_mod_list, client_mod_list):
    server_set = set(server_list)
    client_set = set(client_list)
    
    client_needs = list(server_set - client_set)
    server_needs = list(client_set - server_set)

    #adds files to list of files needed based on date modification
    sim_files = server_set & client_set
    for file in sim_files:
        if server_mod_list[server_list.index(file)] > client_mod_list[client_list.index(file)]:
            client_needs.append(file)
        elif server_mod_list[server_list.index(file)] < client_mod_list[client_list.index(file)]:
            server_needs.append(file)
            
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
    
    
    # server address and port number
    server_address = (HOST, PORT) 
    print("Starting up connection...)")
    #bind to a port
    sock.bind(server_address)
    while True:
        # begins waiting for connections
        sock.listen() 
        clientsocket, address = sock.accept()
        with clientsocket:
            print(f"Connection has been established.")
            while True:
                #list of files in folder
                list_of_files = [file.name for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]
                #list of times when files were modified
                list_of_time_mod = [get_date_modified(file.name) for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]
                #Recieve files that the client has
                data = clientsocket.recv(1024)
                data_mod = clientsocket.recv(1024)
                data = data.decode()
                data_mod = data_mod.decode()
                client_file_list = string_to_list(data)
                client_mod_time = string_to_list(data_mod)
                client_mod_time = [float(date_mod) for date_mod in client_mod_time]
                needed_files_list = compare_files(list_of_files, client_file_list, list_of_time_mod, client_mod_time)
                server_needs = list_to_string(needed_files_list[0]).encode('utf-8')
                client_needs = list_to_string(needed_files_list[1])
                clientsocket.sendall(server_needs)
                print(client_needs)
                if not data:
                    break
