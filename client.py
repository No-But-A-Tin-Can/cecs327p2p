import socket
import sys
import time
import os
import pickle
import threading
import hashlib
import file_access

#Get the host and port to be used
HOST = socket.gethostbyname(socket.gethostname())
#Using a port that is not in use
PORT = 9999

#list of files in the directory at the start
list_of_files = [file.name for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]
encoded_list = '/'.join(list_of_files).encode('utf-8')
#[item.encode('utf-8') for item in list_of_files]
print(encoded_list)

class client:

    def __init__(self, address, hashlist):

        # AF_INET = IPv4 SOCK_STREAM = TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            self.sock.connect((address, PORT))
            self.previousContent = None

            # Setting up threads to send the data to server
            sending_thread = threading.Thread(target=self.send_data)
            sending_thread.daemon = True
            sending_thread.start()

            # Create a hash list to store the peers -- Does not work right now however
            self.hashlist = hashlist

            # Setting up threads to recieve the data from 
            while True:
                time.sleep(2)
                sock.sendall(encoded_list)
                r_thread = threading.Thread(target=self.recieve_message)
                r_thread.start()
                r_thread.join()
                data = sock.recv(1024)
                print('Recieved', repr(data))

                if not data:
                    print("ERROR! Unable to connect!")
                    break
                elif data[0:1] == b'\x11':
                    print("Retrieving Data Fom Peers!")
                    self.update_peers(data[1:])

    # Method to send a message 
    def send_message(self):
        try:
            self.sock.send('req'.encode('utf-8'))
        except KeyboardInterrupt as e:
                print(e)
                return

    # Method will write message into seperate files to the corresponding folder
    def recieve_message(self):
        print("Incoming message being recieved")
        while True:
            msg = self.sock.recv(1024) 

            print(msg.decode("utf-8"))

            print("Message recieved from Server: ")

            if self.previous_data != msg:
                file_access.create_file(msg)
                self.previousContent = msg

            return msg
    
    # Method to update the peer list
    def update_peers(self, peers):
        p2p.peers = str(peers, "utf-8").split(',')[:-1]


                
