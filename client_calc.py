import socket
import signal
import sys

ClientSocket = socket.socket()
host = '192.168.253.12'
port = 8080                     #Change this port number same with server

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    c_input = input('Enter the operation and number: ')
    if c_input == 'q':
        break
    else:
        ClientSocket.send(str.encode(c_input))  #encode the data
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

ClientSocket.close()