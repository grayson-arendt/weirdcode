#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);

int valvePin = 8;
const int pressureInput = A0;
const int pressureZero = 102.4;
const int pressureMax = 921.6;
const int pressuretransducermaxPSI = 100;
float maxSolenoidPressure = 10.5;
float pressureValue;
float newpressureValue;

void setup() {
  Wire.begin();
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);

  pinMode(valvePin,OUTPUT);
  digitalWrite(valvePin,HIGH);
}

void displayPressure() {
  display.clearDisplay();
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.setCursor(0,0);
  delay(1500);
  
  pressureValue = analogRead(pressureInput);
  newpressureValue = ((pressureValue-pressureZero)*pressuretransducermaxPSI)/(pressureMax-pressureZero);
  
  if (newpressureValue > maxSolenoidPressure) {
    digitalWrite(valvePin,LOW); // Opens valve
    display.print("Depressurizing.");
    delay(1000);
    display.clearDisplay();
    display.print("Depressurizing..");
    delay(1000);
    display.clearDisplay();
    display.print("Depressurizing...");
    delay(1000);
    display.clearDisplay();
    display.print("Complete");
    delay(1000);
    display.clearDisplay();
  }
  else {
    digitalWrite(valvePin,HIGH); // Closes valve
    
    display.setCursor(0,0);
    display.print("Pressure Sensor");
    display.setCursor(0,10);
    display.print("Pressure: ");
    display.print(newpressureValue);
    display.print(" psi");
  }
  
}

void loop() {
    displayPressure();
    display.display();
}
  


 
