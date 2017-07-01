#include <ESP8266WiFi.h>
#include <WiFiClient.h> 

String Prefix = "PosNode";
const int X_POS = 1;
const int Y_POS = 0;
const unsigned int NUMBER = 2;
const unsigned char channel = 1;

//It could even be open
String password = "useless password";
String id = Prefix + String(NUMBER) + " " + String(X_POS) + " " + String(Y_POS);

//Pretty useless
void setup(){}

void loop(){
  WiFi.softAP(id.c_str(), password.c_str(), channel);
  delay(1000);
  WiFi.softAPdisconnect();
  delay(1000);
}

