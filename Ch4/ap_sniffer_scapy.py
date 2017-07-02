#AP sniffer scapy edition

from scapy.all import *

interface = 'wlan0mon'
aps = []

def info(frame):
    if((frame.type == 0) & (frame.subtype == 8)):#Just beacons
        if frame.addr2 not in aps:
            aps.append(frame.addr2)
            print "SSID--> ",frame.info,"--BSSID--> ",frame.addr2
sniff(iface = interface, prn = info) #Execute the capture invoking the info function
