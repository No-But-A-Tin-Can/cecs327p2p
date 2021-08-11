## BASED ON SOURCE CODE - https://www.youtube.com/watch?v=3QiPPX-KeSc&t=1406s (Tech with Tim)
import socket
import threading

SERVER = socket.gethostname()  # gethostname() returns the host name for the local machine
PORT = 9999
ADDRESS = (SERVER, PORT)  # Address is comprised of the host name and port

# Creates an INET Streaming Socket
# AF_INET refers to IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind takes in tuple, binding socket to server address
server.bind(ADDRESS)


def startServer():
    print("SERVER STARTING... " + socket.gethostbyname(SERVER))  # socket.gethostbyname() returns the host's IP address
    # Set TCP Backlog; maximum rate at which server can accept new TCP connections on the socket
    server.listen(5)
    print("SERVER LISTENING FOR CONNECTIONS...")
    # Continuous loop accepting new server connections
    while True:
        # Accept new connection to server - Connection (Socket Object) Address (Port & IP Address)
        connection, address = server.accept()
        # Create New Thread for Server Connection
        thread = threading.Thread(target=handleClient, args=(connection, address))
        thread.start()


# Clients looking to establish a connection are passed to this function
# This function would be dedicated to facilitating file synchronization between Client & Server
# Check if files exist on the server-end and send to client if available
# Vice versa if a client was to upload a file to the server, check if file is pre-existing
# before downloading on server-end
def handleClient(connection, address):
    print("ESTABLISHING NEW CONNECTION... " + address[0])


startServer()




