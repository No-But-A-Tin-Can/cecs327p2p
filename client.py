import socket
import sys
import time
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
#test_variable
test_count = 0
# AF_INET = IPv4 SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        time.sleep(2)
        sock.sendall(b'Hello, world!')
        data = sock.recv(1024)
        test_count += 1
        print('Recieved', repr(data))
        if test_count > 100:
            break
            
print("Connection ended.")
