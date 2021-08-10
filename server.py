import socket
import sys
import threading
import time
import os
import pickle

#Get the host and port to be used
HOST = socket.gethostbyname(socket.gethostname())
#Using a port that is not in use
PORT = 9999

list_of_files = [file.name for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]

def __init__(self, contents):

    try:

        print("********Intitializing Server...Please Wait!********")

        self.contents = contents

        self.activePeers = [] # List all active peers
        self.activeNetworks = [] # List all active networks

        # AF_INET = IPv4 SOCK_STREAM = TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            # server address and port number
            server_address = (HOST, PORT) 
            print("Starting up on %s port %s" % server_address)

            #bind to a port
            self.sock.bind(server_address)

        while True:
            # begins waiting for connections
            self.sock.listen(5) 
            clientsocket, address = sock.accept()
            with clientsocket:
                print(f"Connection from {address} has been established.")
                while True:
                    data = clientsocket.recv(1024)
                    data = data.decode()
                    client_file_list = data.split('/')
                    print(client_file_list)
                    print(data)
                    if not data:
                        break
                    clientsocket.sendall(data.encode('utf-8'))
    except Exception as e:
        sys.exit()

def run(self):
        while True:
            clientsocket, address = self.sock.accept()
            self.activePeers.append(address)
            print("LIST OF PEERS: {}".format(self.activePeers))
            self.send_peers()
            c_thread = threading.Thread(target=self.controller, args=(clientsocket, address))
            c_thread.daemon = True
            c_thread.start()
            self.networks.append(clientsocket)
            print("{}, connected".format(address))
            print("-" * 50)

def send_peers(self):
        peer_list = ""
        for peer in self.activePeers:
            peer_list = peer_list + str(peer[0]) + ","

        for network in self.networks:
            data = b'\x11' + bytes(peer_list, 'utf-8')
            network.send( b'\x11'+ bytes(peer_list, 'utf-8'))

