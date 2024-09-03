#include <Arduino.h>
#include "BLEMidiBase.h"

void BLEMidi::begin(const std::string deviceName)
{
    this->deviceName = deviceName;
    BLEDevice::init(deviceName);
}

void BLEMidi::end() {
    BLEDevice::deinit();
}

bool BLEMidi::isConnected()
{
    return connected;
}

void BLEMidi::setBatteryLevel(uint8_t level) {
  this->batteryLevel = level;
  if (hid != 0) {
    this->hid->setBatteryLevel(this->batteryLevel);
  }
}
