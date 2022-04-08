from pynput.keyboard import Key, Controller
import json

import time

time.sleep(5)

keyboard = Controller()
m = open("map_th_en.json", "r", encoding="utf8")
mapTH = json.loads(m.read())

f = open("text.txt", "r", encoding="utf8")

langSwap = False

for i in f.read():
    kInput = i

    if(kInput in mapTH):
        kInput = mapTH[kInput]
        if not langSwap:
            # keyboard.press(Key.ctrl_l)
            # keyboard.press(Key.shift_l)
            # keyboard.press("2")
            # keyboard.release("2")
            # keyboard.release(Key.shift_l)
            # keyboard.release(Key.ctrl_l)
            langSwap = True
            
            keyboard.press(Key.alt_l)
            keyboard.press(Key.shift_l)
            keyboard.release(Key.shift_l)
            keyboard.release(Key.alt_l)
            time.sleep(1)

    elif langSwap:
        # keyboard.press(Key.ctrl_l)
        # keyboard.press(Key.shift_l)
        # keyboard.press("1")
        # keyboard.release("1")
        # keyboard.release(Key.shift_l)
        # keyboard.release(Key.ctrl_l)
        langSwap = False

        keyboard.press(Key.alt_l)
        keyboard.press(Key.shift_l)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.alt_l)
        time.sleep(1)

    if kInput.isupper():
        keyboard.press(Key.shift_l)
        
    if kInput != "\n":
        keyboard.press(kInput.lower())
        keyboard.release(kInput.lower())
    else:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    if kInput.isupper():
        keyboard.release(Key.shift_l)