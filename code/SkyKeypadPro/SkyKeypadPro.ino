#include <Adafruit_Keypad.h>
#include <Adafruit_Keypad_Ringbuffer.h>

#include "src/ESP32-BLE-Keyboard/BleKeyboard.h"

#include "USBVendor.h"
#include "USB.h"
#include "USBHIDKeyboard.h"
#include "USBMIDI.h"
#include "BLEMidi.h"

#define rotA_pin 11
#define rotB_pin 10
#define rotSW_pin 44


USBVendor usbVendor;

USBHIDKeyboard usbKeyboard;
BleKeyboard bleKeyboard;

USBMIDI MIDI;

#define MIDI_NOTE_C4 60

const byte ROWS = 3;
const byte COLS = 5;

const byte rowPins[ROWS] = {8, 7, 6};
const byte colPins[COLS] = {1, 2, 3, 4, 5};


/*
Mode 0 = Keyboard;
Mode 1 = MIDI;
*/
int mode = 0;


/*
Keymap 0 = Sky Music Nightly (web);
Keymap 1 = In-game playback;
*/
int keymap = 0;


/*
Interface Mode 0: None;
Interface Mode 1: USB;
Interface Mode 2: Bluetooth;
*/
int interface = 0;


bool forceUSB = false;
bool forceBT = false;

bool btEnabled = false;
bool btConnected = false;

bool usbStatus = false;

void setup() {
  Serial.begin(115200);
  Serial.println("Starting...");

  pinMode(rotA_pin, INPUT_PULLUP);
  pinMode(rotB_pin, INPUT_PULLUP);

  pinMode(rotSW_pin, INPUT_PULLUP);


  if (forceUSB) {         // Communicate over USB, no matter what
    usbMode()
  }
  else if (forceBT) {     // Communicate over BT, no matter what
    
  }
}

void loop() {
  setMode();
}


void usbMode() {
  if (mode == 0) {
    usbKeyboard.begin();
    USB.begin();
  }
  else if (mode == 1) {

  }
  btEnabled = false;
  interface = 1;
}

void btMode() {
  if (mode == 0) {
    bleKeyboard.begin();
  }
  else if (mode == 1) {
    BLEMidiServer.begin("Sky Music Keypad");
  }
  btEnabled = true;
  interface = 2;
}


void setMode() {
  if (!(forceUSB || forceBT)) {
    usbStatus = usbVendor.mounted();
    if (usbStatus) {            // Is USB connected?
      if (interface != 1) {     // Have we already recorded that we're in USB mode?
        interface = 1;          // Set mode to USB
        bleKeyboard.end();      // Disable Bluetooth while connected to USB
        btEnabled = false;
      }
      return;
    }
    else {                      // Not connected to USB
      if (!btEnabled){          // If Bluetooth is disabled, re-enable it
        bleKeyboard.begin();
        btEnabled = true;
      }
      if (bleKeyboard.isConnected()) {  // Bluetooth device connected!
        interface = 2;
      }
      else {                    // No BT or USB connection
        interface = 0;
      }
    }
  }
}

void sendKey(uint8_t key, bool press = true) {
  if (interface == 0) {
    return;
  }
  else if (interface == 1) {
    if (press) {
      usbKeyboard.press(key);
    }
    else {
      usbKeyboard.release(key);
    }
  }
  else if (interface == 2) {
    if (press) {
      bleKeyboard.press(key);
    }
    else {
      bleKeyboard.release(key);
    }
  }
}






/*
TODO: mostly everything
- add battery level (line 101 in BleKeyboard.cpp)
- add matrix (use hex for keys?)
*/