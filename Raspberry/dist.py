def distance(rssi):
    startStrength = -9
    dBmMeter = 31
    return((-rssi+startStrength)/dBmMeter)
