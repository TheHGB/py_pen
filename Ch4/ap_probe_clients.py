from scapy.all import *

interface = "wlan0mon"
probes = []

ap = raw_input("Enter the AP whose clients you want to find ")

def analyze(probe):
    if probe.haslayer(Dot11ProbeReq): #Only interested in probe requests
        if (probe.info == ap) && (if probe.addr2 not in probes):
            probes.append(probe.addr2)
            print "Client: ", probe.addr2

sniff(iface = interface, prn = analyze)

