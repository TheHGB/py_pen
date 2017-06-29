import socket

host = raw_input("Enter the host you wish to analyze ")
ports = raw_input("Enter the range of the ports you wish to analyze (separated with ,) ")
ran = ports.split(',')
for port in range(int(ran[0]),int(ran[1])+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if (s.connect_ex((host, port)) == 0):
        print "Port", port, "is open"
    s.close()

