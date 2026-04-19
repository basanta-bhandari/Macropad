import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# These are the pins your switches are connected to
# If your switches don't work, double check these against your schematic!
keyboard.col_pins = (board.GP27,)
keyboard.row_pins = (board.GP26, board.GP25, board.GP28)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# KEYMAP - change the keys here to whatever you want!
# Some useful keys:
#   KC.COPY, KC.PASTE, KC.CUT, KC.UNDO, KC.REDO
#   KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.AUDIO_MUTE
#   KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DOWN
#   KC.F1 - KC.F12
#   KC.LGUI(KC.L) = Windows lock screen
#   KC.LCTL(KC.Z) = Ctrl+Z (undo)
#   KC.LCTL(KC.S) = Ctrl+S (save)
#   Full key list: https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/keycodes.md

keyboard.keymap = [
    [
        KC.LCTL(KC.C),   # Key 1: Copy (change me!)
        KC.LCTL(KC.V),   # Key 2: Paste (change me!)
        KC.LGUI(KC.LSFT(KC.S)),  # Key 3: Screenshot on Windows (change me!)
    ]
]

if __name__ == '__main__':
    keyboard.go()