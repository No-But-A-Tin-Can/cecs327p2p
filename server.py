from posix import listdir
import socket
import sys
import threading
import time
import os
import pickle
import filecmp

# Server class -- Server will continue to run while the program is running

#Get the host and port to be used
HOST = socket.gethostbyname(socket.gethostname())
#Using a port that is not in use
PORT = 9999

# shows the list of files being stored
list_of_files = [file.name for file in os.scandir() if file.is_file() and file.name.endswith('.txt')]

class Server:

    def __init__(self, contents):

        try:

            print("********Intitializing Server...Please Wait!********")

            self.contents = contents
            self.activePeers = [] # List all active peers
            self.activeNetworks = [] # List all active networks
            tempFolder = "Temp"  # Store files in a temporary location
            currentWorkingDirectory = os.getcwd() # Gets the path where files are stored
            tempPath = currentWorkingDirectory + "\\" + tempFolder
            try:
                os.makedirs(tempPath) # Creates the folder
            except FileExistsError: # If the folder already exists
                for files in os.listdir(tempPath): # Clears temp folder if there are files stored already
                    os.remove(os.path.join(tempPath, files)) 
                pass

            # NOTES: AF_INET = IPv4 SOCK_STREAM = TCP

            # Creat the server socket to accept client wanting to connect
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows us to reuse the socket

                # server address and port number
                server_address = (HOST, PORT) 
                print("Starting up on %s port %s" % server_address)

                #bind to a port
                self.sock.bind(server_address)

                # Listens for up to 5 max connections in queue
                self.sock.listen(5) 

                print("********Succes! Server Is Running!********")
        except Exception as e:
            sys.exit()

    # Method to run the server
    def runServer(self, tempPath, contents):

            while True:

                # begins waiting for connections, up to 5 maximum 
                self.sock.listen(5) 

                # Accepts incoming connections
                clientsocket, address = self.sock.accept()
                clientThread = threading.Thread(target=self.clientFile, args=(clientsocket, tempPath, contents))
                clientThread.daemon = True
                clientThread.start()
                clientThread.join()
                self.activeNetworks.append(clientsocket) # Adds new connections to the list
                self.activePeers.append(address[0]) # Adds address of new peers to the list
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

    # Method to take the contents of the client and store in the temp folder
    def recieveFiles(self, clientsocket, tempPath, synchronizationPath):
        print("********Downloading Files! Please Wait!********")
        time.sleep(1)
        while True:
            data = clientsocket.recv(1024)
            data = data.decode()
            client_file_list = data.split('/')
            print(client_file_list)
            print(data)
            if not data:
                break
            clientsocket.sendall(data.encode('utf-8'))

            datalist = pickle.loads(data[10:])
            # This will allow the client to send # of files 
            # Otherwise state folder is empty
            if len(datalist) == 0:
                print("ERROR! Folder is empty!")
            else:
                for tempList in datalist:
                    filename = tempList[0] # Recieve the files names
                    tempName = os.path.join(tempPath, filename)

                    # Create the tempFile to write the bytes to send from the client
                    f = open(tempName, 'wb') 
                    f.write(tempList[2]) # Write back files to tempFile
            self.sendFiles(clientsocket, tempPath,synchronizationPath)

    # Method will send back the synchronized folder to the client
    def sendFiles(self, clientsocket, synchronizationPath):
        print("***********Updating Synchronization Folder***********")
        time.sleep(1)
        # Synchronization Folder that will store synced files between clients
        synchronizationFolder = os.listdir(synchronizationPath)
        dataList = []
        for files in synchronizationFolder:
            tempList = []
            tempList.append(files)
            filesize = os.path.getsize(synchronizationPath + "\\" + files)
            tempList.append(filesize)
            with open(synchronizationPath + "\\" + files, "rb" ) as f:
                tempList.append(f.read(tempList[1]))
            dataList.append(tempList)
            pickledList = pickle.dumps(dataList)
            msg = bytes(f'({len(pickledList):<{10}}', "utf-8") + pickledList
            clientsocket.send(msg)


    # Sends a list of peers to all clients showing ip addresses
    def send_peers(self):
            peer_list = ""
            for peer in self.activePeers:
                peer_list = peer_list + ","

            for networks in self.activeNetworks:
                data = b'\x11' + bytes(peer_list, 'utf-8')
                networks.send(data)

