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
falls pip3 nocht nicht installiert ist, hilft ``` sudo apt-get install python3-pip ``` weiter.
 
<br />


Zu guter letzt fehlt noch der der Code, welcher mit ``` git clone https://github.com/Jugendhackt/IPS-FFM.git ``` herunter geladen werden kann.

<br />
Nach Herunterladen der aktuellen Version, kann das Setup mit folgendem Befehl gestartet werden und danach direkt das Programm:

```
nano wifi.py && sudo screen -d python3 IPS-FFM/Raspberry/disp.py
```

In der Wifi.py ist standardmäßig in Zeile 8 die Netzwerkkarte "wlan0" eingetragen. Damit die Berechnungen funktionieren, muss das Siganllevel mit der Einheit "dBm" übergeben werden. Um zu überprüfen ob deine Netzwerkkarte mit unserem Code funktioniert, scanne einmal mit ``` iwlist [interface] scan``` alle Netzwerke und schaue ob das 'Signal level' in "dBm" angeben wird. Solltest du was wie "44/100" finden, funktioniert es leider nicht :(
