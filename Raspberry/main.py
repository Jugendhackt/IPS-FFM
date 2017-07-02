import wifi
import disp
import cor

m = disp.Map()
m.init_screen()

rssi_list = []


while 1:
        rssi_avg = [0,0,0]
        rssi_list = []
        while len(rssi_list) <= 5:
            rssi_list.append(wifi.get_rssi())
        for beacon_n in range(3):
            for i in rssi_list:
                 rssi_avg[beacon_n] += i[beacon_n]
            rssi_avg[beacon_n] = rssi_avg[beacon_n]/5
        print(rssi_avg)
        cordinate = cor.getlocation(1,1,cor.distance(rssi_avg[0])*81.4,350,0,cor.distance(rssi_avg[1])*81.4,350,350,cor.distance(rssi_avg[2])*81.4)
        #print(cor.distance(rssi_avg[2]))
        #print(cordinate)
        m.setObj(cordinate[0], cordinate[1])
