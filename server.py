import socket
import sys

# Creation of a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4 SOCK_STREAM = TCP

server_address = (socket.gethostname(), 9999) # server address and port number
print("Starting up on %s port %s" % server_address)
sock.bind(server_address)

sock.listen(5) # variable used denotes number in a queue

while True:
    clientsocket, address = sock.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Testing testing", "utf-8")) # sending info from server to connected client
