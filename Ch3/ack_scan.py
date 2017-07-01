from scapy.all import *

ip = IP(src = '192.168.1.36', dst = '95.130.49.13')
tcp = TCP(sport = 7896, dport = 113, flags = "A", seq = 1590)
ack = ip/tcp
p = sr1(ack)
p.show()
