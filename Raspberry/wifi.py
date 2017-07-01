import subprocess
import time

class Wifi():
    def __init__(self):
        self.node_list = ["0","1","2"]

    def get_rssi(self, id):
        out = str(subprocess.check_output(["iwlist", "wlan1", "scan"])).split("Cell")
        for i in out:
            if i.find("PosNode"+str(id)) > -1:
           	    return str(i.split("level=",1)[1].split(" ")[0])
        return ""

    def get_rssi_list(self):
        for i in self.node_list:
            printcon(i + ": " + self.get_rssi(i))

def printcon(text):
    o = open("/dev/console","w")
    o.write(text + "\n")

w = Wifi()

while 1:
    w.get_rssi_list()
    time.sleep(1)
