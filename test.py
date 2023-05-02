#!python3
import pyautogui as p


location = p.locateCenterOnScreen('assets/autoclick.png', confidence=0.8)
print('locationOnScreen: ', location)
if location != None:
    p.confirm(text='do you want to buy this?', title='autoclick', buttons=['OK','Cancel'])
    p.moveTo(location)
    p.click()
