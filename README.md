# IPS-FFM
IPS(Indoor Positioning System) ist ein System, mit dem man sich in geschlossenen Räumen zurechtfinden kann.
Man kann es zum Beispiel an Bahnhöfen verwenden, um schnell zum richtigen Gleis zu kommen,
oder beim Messen, um zu einem gesuchten Stand zu kommen.

### Hardware
1. Raspberry Pi
   1. Ladekabel
   2. microSD-Karte
   3. Mobiler Akku/Powerbank
   4. Display
   5. EDIMAX WiFi-Stick
2. 3 ESP8266
   1. Hülle mit Verlinkung
   
 ### Installation
IPS benötigt um lauffähig zu sein zwei Python-Libraries: PyGames und NumPy.

Diese müssen mit pip3 zuerst installiert werden:
```
sudo pip3 install numpy pygames
```

Falls pip3 noch nicht auf dem System installiert ist muss dieses zuerst 
```
sudo apt-get install python3-pip
``` 
Nachdem die Installation der Python-Libraries abgeschlossen ist muss als nächstes die aktuelle Version mit
```
git clone https://github.com/Jugendhackt/IPS-FFM.git
```

Falls git noch nicht installiert ist, muss dieses zuerst installiert werden:
```
sudo apt-get install git
``` 
Nach herunterladen der aktuellen Version, kann das Programm mit folgendem Befehl gestartet werden:
```
sudo screen -d python3 IPS-FFM/Raspberry/disp.py
```
