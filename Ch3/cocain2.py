#The same as the first one but with the data

import socket
import binascii
import struct

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x800))

while True:
    intercept = s.recvfrom(2048)
    eth_header = intercept[0][0:14] 
    ip_header = intercept[0][14:34]
    tcp_header = intercept[0][34:54]
    eth_unpack = struct.unpack("!6s6s2s",eth_header)
    ip_unpack = struct.unpack("12s4s4s", ip_header)
    tcp_unpack = struct.unpack("!HH9ss6s", tcp_header)

    print "---------Ethenrent header-----------"
    print "destination MAC: ", binascii.hexlify(eth_unpack[0])
    print "source MAC: ", binascii.hexlify(eth_unpack[1])
    print "------------IP header--------------"
    print "source IP: ", socket.inet_ntoa(ip_unpack[1])
    print "destination IP: ", socket.inet_ntoa(ip_unpack[2])
    print "------------TCP header--------------"
    print "source port: ", tcp_unpack[0]
    print "destination port: ", tcp_unpack[1]
    print "flags: ", binascii.hexlify(tcp_unpack[3])
    print "--------------Data------------------"
    print intercept[0][54:]


