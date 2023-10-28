import keypad
import board

import random
import time

import rotaryio

import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend

skyNotes = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]

#keys = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

octaveOffset = 0

km = keypad.KeyMatrix(
    row_pins=(board.GP12, board.GP11, board.GP10),
    column_pins=(board.GP6, board.GP5, board.GP4, board.GP3, board.GP2),
    columns_to_anodes=True,
)

enc = rotaryio.IncrementalEncoder(board.GP14, board.GP13)
last_position = None

print(usb_midi.ports)
midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0
)

print("Default output channel:", midi.out_channel + 1)

print("Listening on input channel:", midi.in_channel + 1)

while True:
    position = enc.position
    octaveOffset = position

    event = km.events.get()
    if event:
        #keys[event.key_number] = event.pressed

        note = skyNotes[event.key_number] + octaveOffset
        if event.pressed:
            midi.send(NoteOn(note, 120))
        elif not event.pressed:
            midi.send(NoteOff(note, 120))


    if last_position == None or position != last_position:
        print(position)
    last_position = position

    msg = midi.receive()
    if msg is not None:
        print("Received:", msg, "at", time.monotonic())





while False:
    midi.send(NoteOn(44, 120))  # G sharp 2nd octave
    time.sleep(0.25)
    a_pitch_bend = PitchBend(random.randint(0, 16383))
    midi.send(a_pitch_bend)
    # note how a list of messages can be used
    midi.send([NoteOff("G#2", 120), ControlChange(3, 44)])
    time.sleep(0.5)
    msg = midi.receive()

    if msg is not None:
        print("Received:", msg, "at", time.monotonic())
