import binascii
import socket

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:
    packet = s.recvfrom(2048)
    banner = packet[0][54:533]
    if "Date" in banner:
        print banner
