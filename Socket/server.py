import socket
#Defining the server. Creating server side socket. Argunents can be ipv4 and tcp
server = socket.socket()
print("Server socket created")
#Server side ip address and port number should be mentioned as single argument
server.bind(('127.0.0.1',9999))
#Now start listening for the clients. We have to define the number of clients we will allow
#our servers to listen and if the requests are greater it will refuse the connection.
server.listen(3)
print("Waiting for connections")
#We want the server to listen to the number of clients we defined above so it should 
#stop after first listen In order dto do this repeatedly we will use a 'while' loop
while True:
    #It will accept connection from a client. Which will return two values
    #client socket and its ip address
    client , client_ip = server.accept()
    print(f'Connected with {client_ip}')
    #We will send a message from the server once connection is established.
    server.send(bytes('You have been hacked!!','utf-8'))
    #Close the connection
    server.close()
