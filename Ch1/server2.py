import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12344
s.bind((host,port))
s.listen(10)
while True:
    conn, addr = s.accept()
    print addr,"Now connected"
    conn.send("Dank fur ihre connection")
    conn.close()

