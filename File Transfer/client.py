import socket

s = socket.socket()
host = "127.0.0.1"
port = 5001

s.connect((host, port))
s.send("Hello server!".encode())

with open('recv.txt', 'wb') as f:
   while True:
      print('receiving data...')
      data = s.recv(1024)
      if not data:
         break
      f.write(data)
      
f.close()
print('Successfully received')
s.close()
print('connection closed')