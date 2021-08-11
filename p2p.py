import os
import socket
import sys
from server import Server
import time

class p2p:
    peers = ['127.0.0.1'] # Create a peer list so server and client can utilize it 
    
# Creat a SyncFolder that contains the files to be synced among all peers connected 
def findDirectory(name):
    folderName = name  # the folder name where the files will be stored
    currentWorkingDirectory = os.getcwd()  # Acquire where the program is stored
    path = currentWorkingDirectory + "\\" + folderName
    try:
        os.makedirs(path)  # attempt to create a folder if it does not exists
    except FileExistsError:  # Lets the user know the file already exists
        print("Directory \"%s\" detected" % path)
    else:
        print("Successfully created the directory \"%s\"" % path)

    contents = os.listdir(path)  # Retrieve files in the SyncFolder
    print("Displaying Contents: " % folderName)
    
    if len(contents) == 0:  # If files have nothing stored in them
        print("(ERROR! No files)")
    else:
        for content in contents:  # prints the contents within sync folder
            print(content)
    return path, contents

# Main function 
def main():
    while True:
        # Create the SynchronizationFolder with the path and contents
        synchronizationPath, synchronizationContents = findDirectory("SynchronizationFolder")
        print("System Info: " % (socket.gethostname(), socket.gethostbyname(socket.gethostname())))
        p2p.peers.append(attemptToConnect)
        for peer in p2p.peers:
            try:
                client = client(peer, synchronizationPath, synchronizationContents)
            except KeyboardInterrupt:
                sys.exit(0)
           
            # become server if disconnected from client or unable to become client
            try:
                print("Initializing server...")
                time.sleep(1)
                server = Server(synchronizationPath)
            except KeyboardInterrupt:
                sys.exit(0)


if __name__ == '__main__':
    main()
