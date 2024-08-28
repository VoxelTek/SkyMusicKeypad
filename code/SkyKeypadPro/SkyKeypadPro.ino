/**
 * This example turns the ESP32 into a Bluetooth LE keyboard that writes the words, presses Enter, presses a media key and then Ctrl+Alt+Delete
 */
#include "src/ESP32-BLE-Keyboard/BleKeyboard.h"

#include "USB.h"
#include "USBHIDKeyboard.h"
USBHIDKeyboard usbKeyboard;
BleKeyboard bleKeyboard;

int mode = 0;
/*
Mode 0 = Keyboard, BT or USB
Mode 1 = MIDI, BT or USB
*/

int keymap = 0;
/*
Keymap 0 = Sky Music (web)
Keymap 1 = In-game playback
*/

bool forceUSB = true;
bool forceBT = false;

bool btConnected = true;
const int btTimeoutLength = 5;
int btTimeout = 5;

void setup() {
  Serial.begin(115200);
  Serial.println("Starting...");

  if (!forceBT) {
    usbKeyboard.begin();
    USB.begin();
  }
  if (!forceUSB) {
    bleKeyboard.begin();
  }
}

void loop() {
  if (forceUSB) {
    usbMode();
  }
  else if (forceBT) {
    btMode();
  }
  /*
  else if (btConnected) {
    if (btTimeout > 0) {
      btTimeout -= 1;
      return;
    }
  }

  Serial.println("Waiting 5 seconds...");
  delay(5000);
  */
}


void usbMode() {
  
}

void btMode() {
  
}