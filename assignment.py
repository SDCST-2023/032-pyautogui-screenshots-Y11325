#! python3
import multiprocessing
import pyautogui as p
import time

alarms = [0]
delays = [10]
start = time.time()
alarms[0] = start + delays[0]

def timer():
    while True:
        now = time.time()
        if now > alarms[0]:
            print(f"{delays[0]} second alarm has been triggered (click stuff in menu)")
            alarms[0] = now + delays[0]
        time.sleep(1)
        print(f"time elapsed is {round(time.time() - start,3)}")

def CandyButton():
    time.sleep(0.005)
    location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.85)
    print('CANDY_LOCATION: ', location)
    while True:
        if location == None:
            location = p.locateCenterOnScreen('assets/CANDY.png', confidence = 0.75)
        elif location != None:
            p.moveTo(location)
            while True:
                p.click()


def store():
    while True:
        now = time.time()
        if now > alarms[0]:

            location = []
            timemachine = location.append(p.locateCenterOnScreen('assets/timemachine.png', confidence = 0.85, grayscale = True))
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
            
            break
        else:
            pass


def yellowcandy():
    while True:
        yellowC = p.locateCenterOnScreen('assets/yellow candy.png', confidence = 0.7, grayscale = True)
        if yellowC != None:
                p.moveTo(yellowC[0],yellowC[1], 0.000001)
                p.click()
    #p.pixelMatchesColor((251, 221, 4))
 
def main():
    p.confirm("Click to start")

    process0 = multiprocessing.Process(target = timer)
    process1 = multiprocessing.Process(target = CandyButton)
    #process2 = multiprocessing.Process(target = yellowcandy)
    process3 = multiprocessing.Process(target = store)

    process0.start()
    process1.start()
    #process2.start()
    process3.start()

    process0.join()
    process1.join()
    #process2.join()
    process3.join()



if __name__ == '__main__':
    main()
