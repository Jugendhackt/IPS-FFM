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
IPS benötigt um lauffähig zu sein zwei Python-Libraries: PyGames und NumPy. Wenn es sich bei der Plattform auf der IPS ausgeführt werden soll um einen Raspberry Pi handelt fällt die erste Installation weg, da PyGames auf diesem standardmäßig schon nstalliert ist.

Ansonsten wird dies über
´´´
sudo pip3 install pygames
´´´
installiert.

Anschließend wird NumPy über den Befehl
´´´
sudo pip3 install numpy
´´´
installiert

Falls pip3 noch nicht auf dem System installiert ist muss dieses mit 
´´´
sudo apt-get install python3-pip
´´´ 
zuerst installiert werden.

Nachdem die Installation der Python-Libraries abgeschlossen ist muss als nächstes die aktuelle Version mit
´´´
git clone https://github.com/Jugendhackt/IPS-FFM.git
´´´
heruntergeladen werden. Falls git noch nicht installiert ist, muss dieses mit 
´´´
sudo apt-get install git
´´´ 
zuerst installiert werden.

Nachdem die aktuelle Version heruntergeladen wurde, kann das Programm mit 
´´´
sudo screen -d python3 IPS-FFM/Raspberry/disp.py
´´´
gestartet werden.
