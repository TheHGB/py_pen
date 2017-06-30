import struct
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12346

s.bind((host,port))
s.listen(2)

soketto, addr = s.accept() #You just wached anime, so there goes that

msg = struct.pack('hhl',1,2,3)

soketto.send(msg)
soketto.close()



