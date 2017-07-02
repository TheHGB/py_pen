#This is a cheap version of airodump-ng
import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 3)

s.bind(("wlan0mon", 0x0003))
aps = []

while True:
    tmp = s.recvfrom(6000)
    scann = tmp[0] #Only the headers
    if scann[26] == "\x80": #check if beacon
        if scann[36:42] not in aps: #chek if BSSID in the list
            aps.append(scann[36:42])
            a = ord(scann[63]) #value of the lenght of the SSID
            print "SSID -> ",scann[64:64 +a],"-- BSSID -> ", scann[36:42].encode('hex'),"-- Channel -> ", ord(scann[64 +a+12])
