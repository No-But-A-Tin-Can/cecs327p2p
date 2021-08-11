# BASED ON SOURCE CODE - https://www.youtube.com/watch?v=3QiPPX-KeSc&t=1406s (Tech with Tim)
import socket

HOST = input("Enter Host Address: ")
PORT = 9999
ADDRESS = (HOST, PORT)

# Creates an INET Streaming Socket
# AF_INET refers to IPv4
client = socket.socket()
# Connect Client with Server
client.connect(ADDRESS)

print("CONNECTION ESTABLISHED... " + HOST)




