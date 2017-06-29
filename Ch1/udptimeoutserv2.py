import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
s.bind((host,port))
s.settimeout(5)
try:
    addr, data = s.recvfrom(1024)
    print addr,data
except:
    print "Client not connected"
    s.close()
