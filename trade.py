import webbrowser
import time
import subprocess
#from mouse_rand import mouse
import random
import pyautogui


#
# url = "https://www.bitget.com/spot/PLUMEUSDT?type=spot"
#webbrowser.open(url)
time.sleep(10)
try:
    icon_location1 = pyautogui.locateCenterOnScreen('image/bbo.png', confidence=0.1)
    pyautogui.click(icon_location1)
    #step3
  
    icon_location2 = pyautogui.locateCenterOnScreen('image/counter.png', confidence=0.6)
    pyautogui.click(icon_location2)
 
    #step4
    icon_location3 =pyautogui.click(pyautogui.locateCenterOnScreen('image/queu.png', confidence=0.7))
    pyautogui.click(icon_location3)
    
    #step5
    time.sleep(1)
    icon_location4 = pyautogui.moveTo(1877,501)
    pyautogui.click(icon_location4)
    
    #step6
    time.sleep(1)
    icon_location5 = pyautogui.locateCenterOnScreen('image/buy.png', confidence=0.8)
    #pyautogui.click(icon_location5)
    print("Buy order placed")

    while True:
        try:
            if pyautogui.locateOnScreen("image/open.png", confidence=0.6):
                print("Open orders (0) detected.")
            elif pyautogui.locateOnScreen("image/noorder.png", confidence=0.6):
                break
        except:
            continue

    icon_location6 = pyautogui.locateCenterOnScreen('image/sellside.png', confidence=0.5)
    pyautogui.click(icon_location6)
    print("Click5")
    #step7
    time.sleep(1)
    icon_location7 = pyautogui.locateCenterOnScreen('image/bbo.png', confidence=0.5)
    pyautogui.click(icon_location7)
    print("Click6")
    #step8
    time.sleep(1)
    icon_location8 = pyautogui.locateCenterOnScreen('image/counter.png', confidence=0.5)
    pyautogui.click(icon_location8)
    print("Click7")
    time.sleep(1)
    icon_location4 = pyautogui.moveTo(1877,501)
    pyautogui.click(icon_location4)
    #step9
    time.sleep(0.5)
    icon_location9 = pyautogui.locateCenterOnScreen('image/sell.png', confidence=0.5)
    pyautogui.click(icon_location9)
    print("Sell order placed")
    while True:
        try:
            if pyautogui.locateOnScreen("image/close.png", confidence=0.6):
                print("Open orders (0) detected.")
            elif pyautogui.locateOnScreen("image/noorder.png", confidence=0.6):
                break
        except:
            continue

    time.sleep(1)
    icon_location10 = pyautogui.locateCenterOnScreen('image/buyside.png', confidence=0.5)
    pyautogui.click(icon_location10)

   
except :
    print("image not found")