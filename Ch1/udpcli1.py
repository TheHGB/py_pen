import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
print s.sendto("yelo",(host,port))
s.close()
