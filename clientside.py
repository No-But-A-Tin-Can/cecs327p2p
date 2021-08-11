import socket

def Main():
    #define the host and port to be used
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()#craete the socket
    s.connect((host, port))#bind the socket to port

    filename = input("Enter the Filename ")#get user to input the file they want to access
    if filename != 'q':
        s.send(filename.encode('utf-8'))#send the filename if it exists
        data = s.recv(1024)#check if the file exist
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])#get the file size
            message = input("File exists, " + str(filesize) +"Bytes.Do you want to download it? (Yes/No)?")
            if message == 'Yes':
                s.send("OK")
                f = open('new_'+filename, 'wb')#open file in write binary
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print ("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
                print ("Download Complete!")
                f.close()#close the file
        else:
            print ("File Does Not Exist!")

    s.close()#close the connection

if __name__ == '__main__':
    Main()
