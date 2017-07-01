from scapy.all import *

ip = IP(src = "192.168.1.34", dst = "192.168.1.36")
f = TCP(sport = 12345, dport = 80, flags = "F", seq = 7410)
fin = ip/f
p = sr1(fin)
p.show()
