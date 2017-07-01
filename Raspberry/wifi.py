import subprocess
import time

class Wifi():
    def __init__(self):
        self.node_list = ["0","1","2"]

    def get_rssi(self, id):
        out = str(subprocess.check_output(["iwlist", "wlan0", "scan"])).split("Cell")
        for i in out:
            if i.find("PosNode"+str(id)) > -1:
           	    return int(i.split("level=",1)[1].split(" ")[0])
        return 0

    def get_rssi_list(self):
        for i in self.node_list:
            printcon(i + ": " + str(self.get_rssi(i)))
        printcon("")

def printcon(text):
    o = open("/dev/console","w")
    o.write(text + "\n")

def distance(rssi):
    startStrength = -25
    dBmMeter = 13
    return((-rssi+startStrength)/dBmMeter)


w = Wifi()

while 1:
    w.get_rssi_list()
    time.sleep(1)
