import pyautogui
"""""
image_0 = "image/open.png"
image_1 = "image/open1.png"

if pyautogui.locateOnScreen(image_0, confidence=0.1):
    print("Open orders (0) detected.")
elif pyautogui.locateOnScreen(image_1, confidence=0.1):
    print("Open orders (1) detected.")
else:
    print("Neither image detected.")
"""""

import time

# Wait 5 seconds to move the cursor to the desired position
time.sleep(5)

# Get the current mouse position


#icon_location3 =pyautogui.click(pyautogui.locateCenterOnScreen('image/buy.png', confidence=0.6))
#pyautogui.click(icon_location3)
#print("Click3")
#pyautogui.moveTo(1536, 86)
x, y = pyautogui.position()
print(f"Mouse Position: X={x}, Y={y}")
found_words = []
print(len(found_words))


region =(1450,93,450,753)
screenshot1 = pyautogui.screenshot(region=region)
screenshot1.save("screenshot1.png")
