import socket
server = socket.socket()
server.bind(('localhost',12345))
server.listen()
client, addr = server.accept()
print ("connection request from: " + str(addr))