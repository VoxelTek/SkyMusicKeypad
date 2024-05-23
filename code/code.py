import keypad
import board

import storage
import json

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




# Mode can be "midi" for MIDI output,
# "online" for the online Sky composor
# or "game" for playing in the Sky PC demo
cfgFile = open("config.json", "r")

config = json.load(cgfFile.read())

mode = "game"
print("Mode = " + mode)


skyNotes = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]

keys_online = ["Q", "W", "E", "R", "T", "A", "S", "D", "F", "G", "Z", "X", "C", "V", "B"]
keys_game = ["Y", "U", "I", "O", "P", "H", "J", "K", "L", "SEMICOLON", "N", "M", "COMMA", "PERIOD", "FORWARD_SLASH"]

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

btn = DigitalInOut(board.GP15)
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


elif mode == "online" or mode == "game":
    kbd = Keyboard(usb_hid.devices)
    print("keyboard mode")


while True:
    position = enc.position
    noteOffset = position % 12
    enc.position = noteOffset
    event = km.events.get()
    if event:
        if mode == "midi":
            note = skyNotes[event.key_number] + noteOffset + (octaveOffset * 12)
            if event.pressed:
                midi.send(NoteOn(note, 120))
            elif not event.pressed:
                midi.send(NoteOff(note, 120))

            if last_position is None or position != last_position:
                print(position)
            last_position = position

            msg = midi.receive()
            if msg is not None:
                print("Received:", msg, "at", time.monotonic())

            cur_state = btn.value
            if not cur_state:
                octaveAdjust = False
                while (not cur_state):
                    if position != enc.position:
                        octaveOffset = (enc.position - position)
                        octaveAdjust = True

                if not octaveAdjust:
                    enc.position = 0
                else:
                    enc.position = position


            prev_state = cur_state

        elif mode == "online":
            if event.pressed:
                kbd.press(getattr(Keycode, keys_online[event.key_number], None))
            elif not event.pressed:
                kbd.release(getattr(Keycode, keys_online[event.key_number], None))
        elif mode == "game":
            if event.pressed:
                kbd.press(getattr(Keycode, keys_game[event.key_number], None))
            elif not event.pressed:
                kbd.release(getattr(Keycode, keys_game[event.key_number], None))
