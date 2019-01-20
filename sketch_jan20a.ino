#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal.h>
 
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 6, 5, 4, 3, 2);
 
void setup() 
{
  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  Serial.println("Approximate your card to the reader...");
  Serial.println();

  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
 // lcd.print("hello, world!");

}
void loop() 
{
 // lcd.setCursor(0,1);
 // lcd.print(millis()/1000);
   // Turn off the display:
  //lcd.noDisplay();
  //delay(500);
  // Turn on the display:
  lcd.display();
  delay(500);
  
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  lcd.setCursor(0,0);
  Serial.print("UID tag :");
  lcd.print("UID:");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  content.toUpperCase();
 // if (content.substring(1) == "BD 31 15 2B") //change here the UID of the card/cards that you want to give access
  if (content.substring(1) == "B6 53 21 30")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Cory Norman");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 1");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "36 50 32 05")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Josiah Hicks");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 2");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "B6 63 33 05")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Freddy Christopher");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 3");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "46 C7 5E 05")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Jerry Vargas");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 4");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "C3 96 C9 83")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Hector Lee");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 5");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "D6 AB F9 2F")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Elsie Thorne");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 6");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "26 AD 20 05")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Cora Steele");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 7");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "86 D8 58 05")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Esther Hoffman");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 8");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "B6 ED F3 04")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Gemma Byrne");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 9");
    delay(3000);
    lcd.clear();
  }
  else if (content.substring(1) == "36 8F 56 05")
  {
    lcd.setCursor(0,1);
    lcd.clear();
    lcd.print("Iqra Estrada");
    lcd.setCursor(1,1);
    lcd.print("EmpID : 10");
    delay(3000);
    lcd.clear();
  }
 else   {
    lcd.setCursor(0,1);
    Serial.println(" Access denied");
    lcd.print(" Access denied  ");
    delay(3000);
  }
} 
