#include <Adafruit_Keypad.h>
#include <Adafruit_Keypad_Ringbuffer.h>

#include "src/ESP32-BLE-Keyboard/BleKeyboard.h"

#include "USBVendor.h"
#include "USB.h"
#include "USBHIDKeyboard.h"
#include "src/USBMIDI/USBMIDI.h"
#include "src/ESP32-BLE-MIDI/src/BLEMidi.h"

#define rotA_pin 11
#define rotB_pin 10
#define rotSW_pin 44


USBVendor usbVendor;

static struct USBHIDKeyboard *usbKeyboard = NULL;
static struct BleKeyboard *bleKeyboard = NULL;

static struct USBMIDI *MIDI = NULL;

#define MIDI_NOTE_C4 60

const byte ROWS = 3;
const byte COLS = 5;

const byte rowPins[ROWS] = {8, 7, 6};
const byte colPins[COLS] = {1, 2, 3, 4, 5};

int counter = 0;

const String deviceName = "Sky Music Keypad";


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

bool usbStatus = false;

void setup() {
  Serial.begin(115200);
  Serial.println("Starting...");

  pinMode(rotA_pin, INPUT_PULLUP);
  pinMode(rotB_pin, INPUT_PULLUP);

  pinMode(rotSW_pin, INPUT_PULLUP);

  if (mode == 0) {
    static struct USBHIDKeyboard _usbKeyboard;
    usbKeyboard = &_usbKeyboard;
    static struct BleKeyboard _bleKeyboard;
    bleKeyboard = &_bleKeyboard;
  }
  else if (mode == 1) {
    static struct USBMIDI _MIDI;
    MIDI = &_MIDI;
  }

  if (!forceBT) {         // Initialise USB
    usbInit();
  }
  else if (!forceUSB) {   // Initialise BT
    btInit();
  }

}

void loop() {
  setMode();
  if (interface == 2) {
    sendBattery();
  }
}


void sendBattery() {
  if (mode == 0) {

  }
  else if (mode == 1) {

  }
}


void usbInit() {
  if (mode == 0) {
    usbKeyboard->begin();
    USB.begin();
  }
  else if (mode == 1) {

  }
}

void btInit() {
  if (mode == 0) {
    bleKeyboard->setName(deviceName);
    bleKeyboard->begin();
  }
  else if (mode == 1) {
    BLEMidiServer.begin(deviceName);
  }
  btEnabled = true;
}


void switchToUSB() {
  if (interface != 1) {
    if ((interface == 2) || (btEnabled)) {
        if (mode == 0) {
          bleKeyboard->stopAdvertising();
        }
        else if (mode == 1) {
          
        }
    }
  }
}

void switchToBT() {

}




void setMode() {
  if (!(forceUSB || forceBT)) {
    usbStatus = usbVendor.mounted();
    if (usbStatus) {            // Is USB connected?
      switchToUSB();
      return;
    }
    else {                      // Not connected to USB
      switchToBT();
      if (bleKeyboard->isConnected()) {  // Bluetooth device connected!
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
      usbKeyboard->press(key);
    }
    else {
      usbKeyboard->release(key);
    }
  }
  else if (interface == 2) {
    if (press) {
      bleKeyboard->press(key);
    }
    else {
      bleKeyboard->release(key);
    }
  }
}






/*
TODO: mostly everything
- add battery level (line 101 in BleKeyboard.cpp)
- add matrix (use hex for keys?)
*/