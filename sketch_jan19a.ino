#include "SPI.h"
#include "MFRC522.h"
#define SS_PIN 10
#define RST_PIN 9
#include <LiquidCrystal.h>
LiquidCrystal lcd(7, 6, 5, 4, 3, 2);
MFRC522 rfid(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;
void setup() {
    Serial.begin(9600);
    SPI.begin();
    rfid.PCD_Init();
    lcd.begin(16,2);
    lcd.clear();
    lcd.display();
}
void loop() {
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
    return;
  // Serial.print(F("PICC type: "));
  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
  // Serial.println(rfid.PICC_GetTypeName(piccType));

  // Check is the PICC of Classic MIFARE type
  if (piccType != MFRC522::PICC_TYPE_MIFARE_MINI &&
    piccType != MFRC522::PICC_TYPE_MIFARE_1K &&
    piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
    Serial.println(F("Your tag is not of type MIFARE Classic."));
    return;
  }
  String strID = "";
  for (byte i = 0; i < 4; i++) {
    strID +=
    (rfid.uid.uidByte[i] < 0x10 ? "0" : "") +
    String(rfid.uid.uidByte[i], HEX) +
    (i!=3 ? ":" : "");
  }
  strID.toUpperCase();
  Serial.print("Tap card key: ");
  Serial.println(strID);
  if (strID = "B6:53:21:30") {
    lcd.print("Cory Norman");
    lcd.setCursor(2,1);
    lcd.print("ID : 1");
    delay(3000);
    lcd.clear();
  } 
  if (strID == "36:50:32:05") {
    lcd.print("Josiah Hicks");
    lcd.setCursor(2,1);
    lcd.print("ID : 2");
    delay(3000);
    lcd.clear();
  } 
  if (strID == "B6:63:33:05") {
    lcd.print("Freddy Christopher");
    lcd.setCursor(2,1);
    lcd.print("ID : 3");
    delay(3000);
    lcd.clear();
  } 
  if (strID.indexOf("46:C7:5E:05") >= 0) {
    lcd.print("Jerry Vargas");
    lcd.setCursor(2,1);
    lcd.print("ID : 4");
    delay(3000);
    lcd.clear();
  } 
  if (strID.indexOf("C3:96:C9:83") >= 0) {
    lcd.print("Iqra Estrada");
    lcd.setCursor(2,1);
    lcd.print("ID : 5");
    delay(3000);
    lcd.clear();
  } 
  if (strID.indexOf("D6:AB:F9:2F") >= 0) {
    lcd.print("Hector Lee");
    lcd.setCursor(2,1);
    lcd.print("ID : 6");
    delay(3000);
    lcd.clear();
  } 
  if (strID.indexOf("26:AD:20:05") >= 0) {
    lcd.print("Cora Steele");
    lcd.setCursor(2,1);
    lcd.print("ID : 7");
    delay(3000);
    lcd.clear();
  } 
  if (strID.indexOf("86:D8:58:05") >= 0) {
    lcd.print("Esther Hoffman");
    lcd.setCursor(2,1);
    lcd.print("ID : 8");
    delay(3000);
    lcd.clear();
  }  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}
