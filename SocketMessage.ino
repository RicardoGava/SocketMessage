#include <ESP8266WiFi.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define SSID "*****"
#define PASSWD "*****"
#define SOCK_PORT 24000
#define LCD_ROWS 2
#define LCD_COLUMNS 16
#define LED_PIN 16

LiquidCrystal_I2C lcd(0x27, LCD_COLUMNS, LCD_ROWS);

WiFiServer sockServer(SOCK_PORT);

void setup() {
  Serial.begin(9600);
  while (!Serial);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);
  lcd.init();
  lcd.backlight();
  WiFi.begin(SSID, PASSWD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
  }
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
  sockServer.begin(); // abre a porta 24000
}

void loop() {
  WiFiClient client = sockServer.available();
  if (client) {
    while (client.connected()) {
      while (client.available() > 0) {
        lcd.clear();
        lcd.setCursor(0, 0);
        String received = client.read();
        if (received.length() > LCD_COLUMNS) {
          for (row = 0; row < LCD_ROWS; row++) {
            lcd.setCursor(0, row);
            lcd.print(received.substring(row * LCD_COLUMNS, (row + 1)*LCD_COLUMNS));
          }
        }
        else {
          lcd.print(received);
        }
        if (received == "led on") {
          digitalWrite(LED_PIN, LOW);
        }
        if (received == "led off") {
          digitalWrite(LED_PIN, HIGH);
        }
        Serial.println(received);
      }
      delay(10);
    }
    client.stop(); // acabou a leitura dos dados. Finaliza o client.
  }
}
