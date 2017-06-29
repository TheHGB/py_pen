import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
s.bind((host,port))
data, addr = s.recvfrom(1024)
print "recived from",addr,":",data
s.close()
