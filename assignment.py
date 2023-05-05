#! python3

import pyautogui as p
import time

def click():
    for i in range(200):
        p.click()        
    return

def CandyButton():
    time.sleep(0.025)
    location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.8)
    print('CANDY_LOCATION: ', location)
    while True:
        if location == None:
            location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.75)
        elif location != None:
            p.moveTo(location)
            click()
            break
    return

def images():
    candyrocket = (p.locateCenterOnScreen('assets/candyrocket.png', confidence = 0.85, grayscale = True))
    diamondcursor = (p.locateCenterOnScreen('assets/diamondcursor.png', confidence = 0.85, grayscale = True))
    candytemple = (p.locateCenterOnScreen('assets/candytemple.png', confidence = 0.85, grayscale = True))
    candylab = (p.locateCenterOnScreen('assets/candylab.png', confidence = 0.85, grayscale = True))
    goldcursor = (p.locateCenterOnScreen('assets/goldcursor.png', confidence = 0.85, grayscale = True))
    candyfactory = (p.locateCenterOnScreen('assets/candyfactory.png', confidence = 0.85, grayscale = True))
    candymine = (p.locateCenterOnScreen('assets/candymine.png', confidence = 0.85, grayscale = True))
    candyfarm = (p.locateCenterOnScreen('assets/candyfarm.png', confidence = 0.85, grayscale = True))
    steelcursor = (p.locateCenterOnScreen('assets/steelcursor.png', confidence = 0.85, grayscale = True))
    autocandy = (p.locateCenterOnScreen('assets/autocandy.png', confidence = 0.85, grayscale = True))
    cursor = (p.locateCenterOnScreen('assets/cursor.png', confidence = 0.85, grayscale = True))
    autoclick = (p.locateCenterOnScreen('assets/autoclick.png', confidence = 0.85, grayscale = True))

    return candyrocket, diamondcursor, candytemple, candylab, goldcursor, candyfactory, candymine, candyfarm, steelcursor, autocandy, cursor, autoclick

def store(cRocket,dCursor,cTemple,cLab,gCursor,cFactory,cMine,cFarm,sCursor,aCandy,Cursor,aClick):
    location = [cRocket,dCursor,cTemple,cLab,gCursor,cFactory,cMine,cFarm,sCursor,aCandy,Cursor,aClick]

    for i in location:
        if i == None:
            pass
        elif i != None:
            p.moveTo(i[0],i[1], 0.025)
            p.click()
    main()
    return 

def main():
    while True:
        CandyButton()
    cRocket,dCursor,cTemple,cLab,gCursor,cFactory,cMine,cFarm,sCursor,aCandy,Cursor,aClick = images()
    #store(cRocket,dCursor,cTemple,cLab,gCursor,cFactory,cMine,cFarm,sCursor,aCandy,Cursor,aClick)
    return

if __name__ == "__main__":
    p.confirm("Click to start")
    main()