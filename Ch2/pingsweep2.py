import os
print "This is el saner pachangero to ping a range of ips"
net = raw_input("Enter your network ")
sp = net.split('.')
network = sp[0]+'.'+sp[1]+'.'+sp[2]+'.'
first = raw_input("Now enter the first IP (or it's last number) ")
last = raw_input("And the last one ")
for x in range(int(first), int(last)+1):
    obj = network+str(x)
    res = os.system('ping -c 1 '+obj+ ' &> /dev/null')
    if res == 0:
        print "Host ",obj," is up"

