#! python3

import pyautogui as p
import time

def CandyButton():
    global candies
    candies = 0
    location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.8)
    print('locationOnScreen: ', location)
    if location != None:
        p.moveTo(location)
        while True:
            candies += 1
            p.click()
            if candies == 15:
                break
    return

def autoclick():
    location = p.locateCenterOnScreen('assets/autoclick.png', confidence = 0.8)
    print('locationOnScreen: ', location)
    if location != None:
        p.confirm(text='do you want to buy this?', title='autoclick', buttons=['OK','Cancel'])
        p.moveTo(location)
        p.click()
        main()

def okbox():
    p.locateCenterOnScreen('assets/messagebox.png', confidence = 0.8)
    location = p.locateCenterOnScreen('assets/OK.png', confidence = 0.8)
    print('locationOnScreen: ', location)
    if location != None:
        p.moveTo(location)
        p.click()
        main()

def main():
    CandyButton()
    autoclick()
    okbox()

if __name__ == "__main__":
    main()