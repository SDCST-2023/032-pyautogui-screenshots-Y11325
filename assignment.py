#! python3

import pyautogui as p
import time


def CandyButton():
    time.sleep(0.005)
    location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.85)
    print('CANDY_LOCATION: ', location)
    while True:
        if location == None:
            location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.75)
        elif location != None:
            p.moveTo(location)
            for i in range(200):
                p.click()
            break
    return


def store():
    location = []
    candyrocket = location.append(p.locateCenterOnScreen('assets/candyrocket.png', confidence = 0.85, grayscale = True))
    diamondcursor = location.append(p.locateCenterOnScreen('assets/diamondcursor.png', confidence = 0.85, grayscale = True))
    candytemple = location.append(p.locateCenterOnScreen('assets/candytemple.png', confidence = 0.85, grayscale = True))
    candylab = location.append(p.locateCenterOnScreen('assets/candylab.png', confidence = 0.85, grayscale = True))
    goldcursor = location.append(p.locateCenterOnScreen('assets/goldcursor.png', confidence = 0.85, grayscale = True))
    candyfactory = location.append(p.locateCenterOnScreen('assets/candyfactory.png', confidence = 0.85, grayscale = True))
    candymine = location.append(p.locateCenterOnScreen('assets/candymine.png', confidence = 0.85, grayscale = True))
    candyfarm = location.append(p.locateCenterOnScreen('assets/candyfarm.png', confidence = 0.85, grayscale = True))
    steelcursor = location.append(p.locateCenterOnScreen('assets/steelcursor.png', confidence = 0.85, grayscale = True))
    autocandy = location.append(p.locateCenterOnScreen('assets/autocandy.png', confidence = 0.85, grayscale = True))
    cursor = location.append(p.locateCenterOnScreen('assets/cursor.png', confidence = 0.85, grayscale = True))
    autoclick = location.append(p.locateCenterOnScreen('assets/autoclick.png', confidence = 0.85, grayscale = True))

    for i in location:
        if i == None:
            pass
        elif i != None:
            p.moveTo(i[0],i[1], 0.005)
            p.click()
    main()
    return 


def yellowcandy():
    yellowC = p.locateCenterOnScreen('assets/yellow candy.png', confidence = 0.7, grayscale = True)
    if yellowC != None:
            p.moveTo(yellowC[0],yellowC[1], 0.000001)
            p.click()

    #p.pixelMatchesColor((251, 221, 4))
    return
 

def main():
    CandyButton()
    store()
    return


if __name__ == "__main__":
    p.confirm("Click to start")
    main()
