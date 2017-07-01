import subprocess
import time

node_list = [0,1,2]

def get_rssi():
    rssi_list = []
    out = str(subprocess.check_output(["iwlist", "wlan0", "scan"])).split("Cell")
    for devices in out:
        for nodes in node_list:
            if devices.find("PosNode"+str(nodes)) > -1:
                rssiv = int(devices.split("level=",1)[1].split(" ",1)[0])
                rssi_list.append(rssiv)
    return rssi_list

def get_rssi_list():
    for i in node_list:
        printcon(i + ": " + str(distance(get_rssi(i))))
    printcon("")

def printcon(text):
    o = open("/dev/console","w")
    o.write(text + "\n")
