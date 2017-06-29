import os
import platform
import socket
import subprocess
import sys
import threading

network = raw_input("Enter the network you want to scan ")
sp_net = network.split('.')
net = sp_net[0] + '.' + sp_net[1] + '.' + sp_net[2] + '.'
start = int(raw_input("Enter the first IP of the range to analyze "))
end = int(raw_input("Enter the last IP of the range to analyze "))
OS = platform.system()

if (OS == "Windows"):
    pi = "ping -n 1 "
elif (OS == "Linux"):
    pi = "ping -c 1 "
else:
    pi = "ping -c 1 "

class elThread (threading.Thread):
    def __init__(self, st, en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en
    def run(self):
        run1(self.st, self.en)
def run1(st1,en1):
    for ip in range(st1,en1):
        addr = net + str(ip)
        ping = pi + addr + " &> /dev/null"
        res = os.system(ping)
        if (res == 0):
            print addr, "is alive"

all_ips = end - start
ips_x_th = 10
total_th = all_ips / ips_x_th + 1 
los_threads = []
try:
    for i in range(total_th):
        ending = start + ips_x_th
        if (ending > end):
            ending = end
        thread = elThread(start, ending)
        thread.start()
        los_threads.append(thread)
        start = ending
except:
    print "Thread decided he ain't doin shit"

print "Active threads:", threading.activeCount()

for th in los_threads:
    th.join()
