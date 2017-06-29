import socket as sock
s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
host = '127.0.0.1'
port = 12344
s.connect((host,port))
buf = bytearray("-"*30)
print 'number of bytes', s.recv_into(buf)
print buf
s.close()
