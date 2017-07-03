from scapy.all import *

interface = raw_input("Enter the interface you'll work with ")
packets = int(raw_input("Enter the number of packets you'll send "))

eth = Ether(src = RandMAC(), dst = 'FF:FF:FF:FF:FF:FF')
arp = ARP(pdst = '192.168.1.255', hwdst = 'FF:FF:FF:FF:FF:FF')

sendp(eth/arp, iface = interface, count = packets, inter = 0.001)



