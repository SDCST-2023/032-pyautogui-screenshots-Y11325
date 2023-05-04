#! python3

import pyautogui as p
import time

def click():
    while True:
        p.click()

def CandyButton():
    time.sleep(0.05)
    location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.8)
    print('CANDY_LOCATION: ', location)
    while True:
        if location == None:
            location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.75)
        elif location != None:
            p.moveTo(location)
            for i in range(100):
                p.click()
            break
    
    return
def store2():
    candyrocket = (p.locateCenterOnScreen('assets/candyrocket.png', confidence = 0.9))

    diamondcursor = (p.locateCenterOnScreen('assets/diamondcursor.png', confidence = 0.9))

    candytemple = (p.locateCenterOnScreen('assets/candytemple.png', confidence = 0.9))

    candylab = (p.locateCenterOnScreen('assets/candylab.png', confidence = 0.9))

    goldcursor = (p.locateCenterOnScreen('assets/goldcursor.png', confidence = 0.9))

    candyfactory = (p.locateCenterOnScreen('assets/candyfactory.png', confidence = 0.9))

    candymine = (p.locateCenterOnScreen('assets/candymine.png', confidence = 0.9))

    candyfarm = (p.locateCenterOnScreen('assets/candyfarm.png', confidence = 0.9))

    steelcursor = (p.locateCenterOnScreen('assets/steelcursor.png', confidence = 0.9))

    autocandy = (p.locateCenterOnScreen('assets/autocandy.png', confidence = 0.9))

    cursor = (p.locateCenterOnScreen('assets/cursor.png', confidence = 0.9))

    autoclick = (p.locateCenterOnScreen('assets/autoclick.png', confidence = 0.9))

    return candyrocket, diamondcursor, candytemple, candylab, goldcursor, candyfactory, candymine, candyfarm, steelcursor, autocandy, cursor, autoclick

def store(cr,dc,ct,cl,gc,cfac,cm,cfarm,sc,ac,c,aucl):
    location = [cr,dc,ct,cl,gc,cfac,cm,cfarm,sc,ac,c,aucl]

    for i in location:
        if i != None:
            p.moveTo(i[0],i[1], 0.5)
            p.click()
        elif i == None:
            main()
    main()
    return 

def main():
    CandyButton()
    cr,dc,ct,cl,gc,cfac,cm,cfarm,sc,ac,c,aucl = store2()
    store(cr,dc,ct,cl,gc,cfac,cm,cfarm,sc,ac,c,aucl)

if __name__ == "__main__":
    p.confirm("Click to start")
    main()