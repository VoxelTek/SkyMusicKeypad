import usb_cdc
import supervisor

import storage
import json

import keypad
import board

import random
import time

import rotaryio

import usb_hid

import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend
from digitalio import DigitalInOut, Direction, Pull

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayout


serial = usb_cdc.data

global config

with open('config.json') as f:
    config = json.load(f)


mode = config["mode"]
print("Mode = " + mode)


skyNotes = config["midi"]

keyModes = config["modes"]

#keys_online = config["modes"]["online"]
#keys_game = config["modes"]["game"]

#keys = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

noteOffset = 0
octaveOffset = 0

km = keypad.KeyMatrix(
    row_pins=(board.GP8, board.GP9, board.GP10),
    column_pins=(board.GP14, board.GP15, board.GP26, board.GP27, board.GP28),
    columns_to_anodes=True,
)

enc = rotaryio.IncrementalEncoder(board.GP5, board.GP6)
last_position = None

btn = DigitalInOut(board.GP4)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

prev_state = btn.value

if mode == "midi":
    print(usb_midi.ports)
    midi = adafruit_midi.MIDI(
        midi_in=usb_midi.ports[0],
        in_channel=0,
        midi_out=usb_midi.ports[1],
        out_channel=0
    )

    print("Default output channel:", midi.out_channel + 1)

    print("Listening on input channel:", midi.in_channel + 1)

    midi.send(ControlChange(0x10, 0))


else:
    kbd = Keyboard(usb_hid.devices)
    layout = KeyboardLayout(kbd)
    print("keyboard mode")


def writeConfig():
    storage.remount("/", readonly=False)
    cfgFile = open('config.json', "w")
    json.dump(config, cfgFile)
    supervisor.reload()


def sendjson(stream):
    serial.write((json.dumps(stream) + '\n').encode('utf-8'))


def decodeData(data):
    global config

    data = json.loads(data)
    print(data)
    if data['type'] == 'ping':
        pingResponse = {"type": "pong"}
        sendjson(pingResponse)
    elif data['type'] == 'getcfg':
        configResponse = {"type": "config", "cfgdata": config}
        sendjson(configResponse)
    elif data['type'] == 'setcfg':
        config = data["cfgdata"]
        writeConfig()


def checkSerial():
    if serial.in_waiting > 0:
        print(serial.in_waiting)
        data = serial.readline()
        data = data.decode('utf-8').strip()
        print(data)
        decodeData(data)


while True:
    checkSerial()
    position = enc.position
    noteOffset = position % 12
    enc.position = noteOffset
    event = km.events.get()
    if mode == "midi":
        if last_position is None or position != last_position:
                print(position)
                midi.send(ControlChange(0x10, noteOffset))
            last_position = position

        msg = midi.receive()
        if msg is not None:
            print("Received:", msg, "at", time.monotonic())

        cur_state = btn.value # Get if button is pushed
        if not btn.value:
            octaveAdjust = False
            while (not btn.value):
                if position != enc.position:
                    octaveOffset = (enc.position - position)
                    octaveAdjust = True

            if not octaveAdjust:
                enc.position = 0
            else:
                enc.position = position
        prev_state = cur_state


    if event:
        if mode == "midi":
            note = skyNotes[event.key_number] + noteOffset + (octaveOffset * 12)
            if event.pressed:
                midi.send(NoteOn(note, 120))
            elif not event.pressed:
                midi.send(NoteOff(note, 120))
        else:
            if event.pressed:
                kbd.press(layout.keycodes(keyModes[mode][event.key_number])[0])
            elif not event.pressed:
                kbd.release(layout.keycodes(keyModes[mode][event.key_number])[0])
