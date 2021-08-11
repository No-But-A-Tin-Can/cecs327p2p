import socket
import threading
import os

#A threading funcion
def RetrFile(name, sock):
    filename = sock.recv(1024)#set the byte size to be received
    if os.path.isfile(filename):
        #check existence of the file to be shared
        sock.send(b"EXISTS " + bytes(os.path.getsize(filename)))
        userResponse = sock.recv(1024).decode('utf-8')
        if userResponse[:2] == 'OK':
            #open the connection 
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR ".encode('utf-8'))#send the errors 

    sock.close()#close the connection

def Main():
    #define the host and port to be used 
    host = '127.0.0.1' 
    port = 5000


    s = socket.socket()#craete the socket
    s.bind((host,port))# bind the socket to port

    s.listen(5)#set the socket to listen

    print ("The Server Is Started.")
    while True:
        c, addr = s.accept()
        print ("The client connedted ip is: " + str(addr))
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
         
    s.close()# close the connection

if __name__ == '__main__':
    Main()
