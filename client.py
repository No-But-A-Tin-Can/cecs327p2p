import socket
import sys

# Creation of a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4 SOCK_STREAM = TCP

sock.connect((socket.gethostbyname(socket.gethostname()), 9999))

full_msg = ''
while True:
    msg = sock.recv(1024)
    print(len(msg))
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
