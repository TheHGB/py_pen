import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host,port))
print s.recv(1024)
s.send("Hello server")
s.close()
