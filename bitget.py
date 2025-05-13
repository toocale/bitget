import easyocr
import pyautogui
import cv2
import numpy as np
import time
import ast

pyautogui.FAILSAFE = False
# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Load English language model
screenshot = pyautogui.screenshot()
#region =(1450,93,450,753)
#screenshot1 = pyautogui.screenshot(region=region)
screenshot.save("screenshot2.png")
screenshot_np = np.array(screenshot)  # Convert to NumPy array
screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)  # Convert to RGB
def buyorder():
    # Perform OCR and get bounding box data
    results = reader.readtext(screenshot_rgb)

    # List of target words to find
    target_words = ["BBO", "SELL", "BUY" ,"100%","Queue5","Counterparty5", "(1)" ,"100","(2)","(3)" ,"(4)" ,"(5)"]

    # Store found words and their coordinates
    found_words = []

    # Iterate through detected text
    for (bbox, text, prob) in results:
        for target_word in target_words:
            if target_word.lower() in text.lower():
                # Get bounding box coordinates
                (x_min, y_min), (x_max, y_max) = bbox[0], bbox[2]
                center_x, center_y = (x_min + x_max) // 2, (y_min + y_max) // 2  # Find center of the word

                # Store the word and its coordinates
                found_words.append((target_word, center_x, center_y))

    # Move the cursor to each detected word
    print(found_words)
    converted_data = [(word, int(x), int(y)) for word, x, y in found_words]
    converted_data = sorted(converted_data, key=lambda x: x[2] if x[0] == 'BUY' else float('inf'))
    for i, (word, x, y) in enumerate(converted_data):
        if word == "BUY":
            converted_data[i] = ("BUYSIDE", x, y)
              # Stop after renaming the first occurrence
            break
    for i, (word, x, y) in enumerate(converted_data):
        if  word == "100%":
            converted_data[i] = ("100%", x, y-40)
            # Stop after renaming the first occurrence
            break



    print(converted_data)
    # Sample data
    bbo_y = next(y for word, _, y in converted_data if word == "BBO")

    # Extract x from the first BUY
    buy_x = next(x for word, x, _ in converted_data if word == "BUY")
    counterpart=("counterpart", buy_x,bbo_y)
    converted_data.append(counterpart)
    #for queue5 cordinates in
    counterpart_y = next(y for word, _, y in converted_data if word == "counterpart")
    # Extract x from the first BUY
    buy_x = next(x for word, x, _ in converted_data if word == "BUY")
    buy_y = next(y for word, _, y in converted_data if word == "BUY")
    queue = ("queue",buy_x,int((buy_y-counterpart_y)*0.64 + counterpart_y))
    converted_data.append(queue)

   
        # Define sorting priority
    priority = {"BBO": 1, "counterpart": 2, "queue": 3, "100": 4,"BUYSIDE":5,"100%":6,"BUY":7,"SELL":8}
    
    sorted_data = sorted(converted_data, key=lambda x: (priority.get(x[0], 5), x[2] if x[0] == "BUY" else 0))
    # Print sorted list
    print(sorted_data)
    with open("sellside.txt","w")as file:
        file.writelines(str(sorted_data))
    
    for word, x, y in sorted_data:
        pyautogui.moveTo(x, y, duration=0.5)
        print(f"Moved cursor to '{word}' at ({x}, {y})")
        pyautogui.click()
        time.sleep(1)  # Pause for visibility
    print("buy order placed successfully")

    if not found_words:
        print("No target words found on the screen.")

def openorder():
    while True:
        time.sleep(5)
        region =(25,771,192,200)
        screenshot1 = pyautogui.screenshot(region=region)
        screenshot_np1 = np.array(screenshot1)  # Convert to NumPy array
        screenshot_rgb1 = cv2.cvtColor(screenshot_np1, cv2.COLOR_BGR2RGB) 
        # Perform OCR and get bounding box data
        results1 = reader.readtext(screenshot_rgb1)
        # List of target words to find
        target_words = [ "(1)" , "(2)" , "(3)" ,]
        # Store found words and their coordinates
        found_words = []
        for (bbox, text, prob) in results1:
            for target_word in target_words:
                if target_word.lower() in text.lower():
                    # Get bounding box coordinates
                    (x_min, y_min), (x_max, y_max) = bbox[0], bbox[2]
                    center_x, center_y = (x_min + x_max) // 2, (y_min + y_max) // 2  # Find center of the word

                    # Store the word and its coordinates
                    found_words.append((target_word, center_x, center_y))
        if len(found_words) == 0:
            print("open order not found")
            break
        else:
            print("open order found")
def sellorder():
    with open("sellside.txt","r") as file:
        data = file.readline().strip()
        data_read = ast.literal_eval(data)
        priority = {"BBO": 1, "counterpart": 2, "queue": 3, "100": 4,"100%":5,"BUY":6 ,"SELL":7 ,"BUYSIDE":8}
        sorted_data = sorted(data_read, key=lambda x: (priority.get(x[0], 5), x[2] if x[0] == "BUY" else 0))
        for word, x, y in sorted_data:
            pyautogui.moveTo(int(x), int(y), duration=0.5)
            print(f"Moved cursor to '{word}' at ({x}, {y})")
            pyautogui.click()
            
        print("sell order placed successfully")

while True:
    buyorder()
    openorder()
    sellorder()
    openorder()
    time.sleep(2)  # Wait for 10 seconds before starting again