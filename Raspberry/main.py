import wifi
import disp
import cor

m = disp.Map()
m.init_screen()

while 1:
        rssi = wifi.get_rssi()
        cordinate = cor.getlocation(1,1,cor.distance(rssi[0])*81.4,350,0,cor.distance(rssi[1])*81.4,350,350,cor.distance(rssi[2])*81.4)
        m.setObj(cordinate[0], cordinate[1])
