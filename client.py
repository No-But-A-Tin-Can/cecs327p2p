import socket
import sys

# Creation of a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4 SOCK_STREAM = TCP

sock.connect((socket.gethostname(), 10000))

msg = sock.recv(1024)
print(msg.decode("utf-8"))
