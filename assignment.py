#! python3

import pyautogui as p
import time

def click():
    while True:
        p.click()

def CandyButton():
    location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.8)
    print('locationOnScreen: ', location)
    if location != None:
        p.moveTo(location)
        p.click()
    return

def store():
    location = []
    location1 = location.append(p.locateCenterOnScreen('assets/autoclick.png', confidence = 0.8))
    location2 = location.append(p.locateCenterOnScreen('assets/cursor.png', confidence = 0.8))
    
    for i in location:
        print(i)
        print('locationOnScreen: ', location)
        if i != None:
            p.moveTo(i)
            p.click()
    return 

def main():
    CandyButton()
    store()

if __name__ == "__main__":
    p.confirm("Click to start")
    main()