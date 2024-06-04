import usb_cdc
import storage
import board, digitalio

debug = digitalio.DigitalInOut(board.GP4)
debug.pull = digitalio.Pull.UP


if debug.value:
    usb_cdc.enable(console=False, data=True)
    storage.disable_usb_drive()
else:
    usb_cdc.enable(console=True, data=True)

debug = None
