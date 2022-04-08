from pynput.keyboard import Key, Controller
import json
import time

def main():
    time.sleep(5)

    keyboard = Controller()
    mapTH = json.loads(getMapTH())

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
                time.sleep(0.1)

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
            time.sleep(0.1)

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

def getMapTH():
    return '''
    {
    "ๅ" : "1",
    "ภ" : "4",
    "ถ" : "5",
    "ุ" : "6",
    "ึ" : "7",
    "ค" : "8",
    "ต" : "9",
    "จ" : "0",
    "ข" : "-",
    "ช" : "=",
    "ๆ" : "q",
    "ไ" : "w",
    "ำ" : "e",
    "พ" : "r",
    "ะ" : "t",
    "ั" : "y",
    "ี" : "u",
    "ร" : "i",
    "น" : "o",
    "ย" : "p",
    "บ" : "[",
    "ล" : "]",
    "ฃ" : "\",
    "ฟ" : "a",
    "ห" : "s",
    "ก" : "d",
    "ด" : "f",
    "เ" : "g",
    "้" : "h",
    "่" : "j",
    "า" : "k",
    "ส" : "l",
    "ว" : ";",
    "ง" : "'",
    "ผ" : "z",
    "ป" : "x",
    "แ" : "c",
    "อ" : "v",
    "ิ" : "b",
    "ื" : "n",
    "ท" : "m",
    "ม" : ",",
    "ใ" : ".",
    "ฝ" : "/",
    "๑" : "@",
    "๒" : "#",
    "๓" : "$",
    "๔" : "%",
    "ู" : "^",
    "฿" : "&",
    "๕" : "*",
    "๖" : "(",
    "๗" : ")",
    "๘" : "_",
    "๙" : "+",
    "๐" : "Q",
    "ฎ" : "E",
    "ฑ" : "R",
    "ธ" : "T",
    "ํ" : "Y",
    "๊" : "U",
    "ณ" : "I",
    "ฯ" : "O",
    "ญ" : "P",
    "ฐ" : "{",
    "ฅ" : "|",
    "ฤ" : "A",
    "ฆ" : "S",
    "ฏ" : "D",
    "โ" : "F",
    "ฌ" : "G",
    "็" : "H",
    "๋" : "J",
    "ษ" : "K",
    "ศ" : "L",
    "ฉ" : "C",
    "ฮ" : "V",
    "ฺ" : "B",
    "์" : "N",
    "ฒ" : ",",
    "ฬ" : ".",
    "ฦ" : "/"
    }
    '''

main()