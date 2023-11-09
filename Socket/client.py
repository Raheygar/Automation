import socket
#Create client side socket
client = socket.socket()
#Connect to the server
client.connect(('127.0.0.1',9999))
#Receiveing data from the server
output = client.recv(10000).decode()
print(output)