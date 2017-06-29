import os
import socket
print "This is el saner pachangero to ping a range of ips"
net = raw_input("Enter your network ")
sp = net.split('.')
network = sp[0]+'.'+sp[1]+'.'+sp[2]+'.'
first = raw_input("Now enter the first IP (or it's last number) ")
last = raw_input("And the last one ")
port = raw_input("Enter the port you want to discover ")
for x in range(int(first), int(last)+1):
    obj = network+str(x)
    res = os.system('ping -c 1 '+obj+ ' &> /dev/null')
    if res == 0:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((obj,int(port))) == 0:
            print "Host ",obj," is up with the port " + port + " open"
        else:
            print "Host ",obj," is up with the port " + port + " closed"
        s.close()
