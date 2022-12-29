import pyautogui
import time
time.sleep(4)

count = 0
while count <=10:
    pyautogui.typewrite("virual" + str(count))
    count++
    pyautogui.press("enter")
