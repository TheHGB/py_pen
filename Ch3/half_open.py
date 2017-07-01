from scapy.all import *

ip1 = IP(src = "192.168.1.34", dst = "") #put on dst the objetive 

tcp1 = TCP(sport = 1234, dport = 80, flags = "S", seq = 23456) #change dport depending on the port you want to check
syn = ip1/tcp1
elsyn = sr1(syn, inter = 1)
elsyn.show()

rs1 = TCP(sport = 1234, dport = 80, flags = "R", seq = 23458)
reset = ip1/rs1
elreset = sr1(reset)
elreset.show()
