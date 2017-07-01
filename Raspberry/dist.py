def distance(rssi):
    startStrength = -25
    dBmMeter = 13
    return((-rssi+startStrength)/dBmMeter)
