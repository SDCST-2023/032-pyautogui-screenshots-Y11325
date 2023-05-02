#! python3

import pyautogui as p
import time

def CandyButton():
    location = p.locateCenterOnScreen('assets/CANDY.png', confidence=0.85)
    print('locationOnScreen: ', location)
    if location != None:
        p.moveTo(location)
        while True:
            p.click(interval=0)
            if p.click() == 15:
                break
    return

def autoclick():
    location = p.locateCenterOnScreen('assets/autoclick.png', confidence=0.8)
    print('locationOnScreen: ', location)
    if location != None:
        p.confirm(text='do you want to buy this?', title='autoclick', buttons=['OK','Cancel'])
        p.moveTo(location)
        p.click()


def main():
    CandyButton()
    autoclick()


if __name__ == "__main__":
    main()