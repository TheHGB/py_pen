#I know this is really simple (I skip doing the database and the error control) but this was just to learn and to have a little fun and I did not feel like writting a 'really good' script, just an OK one

import threading
import socket
import thread

class TheTread (threading.Thread):
    def __init__(self, ip, start, end):
        threading.Thread.__init__(self)
        self.ip = ip
        self.starting = start
        self.end = end
    def run(self):
        scan(self.ip, self.starting, self.end)

def scan(ip,start,end):
    for port in range(start,end):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if (s.connect_ex((ip, port)) == 0):
            print "Port", port, "is open"
        s.close()
        
temp = raw_input("Enter the IP or the name of the objetive ")
if (len(temp.split('.')) == 4):
    ip = temp
else:
    ip = socket.gethostbyname(temp)

rangue = raw_input("Enter the range of the ports you wish to analyze (separated with <,>) ")

ran = rangue.split(',')

ports_x_th = int(raw_input("Enter the number of ports per thread you'll use (to test speed 'n stuffs) "))


num_th = ((int(ran[1])+1)-int(ran[0])) / ports_x_th + 1#You could have assigned the ran[] to a variable, but you are an idiot and now you want to commit to your idiocy
threads = []
start = int(ran[0])
end = int(ran[1])
for i in range(num_th):
    ending = start + ports_x_th
    if (ending > end):
        ending = end
    thread = TheTread(ip,start,ending)
    thread.start()
    threads.append(thread)
    start = ending
for th in threads:
    th.join()
