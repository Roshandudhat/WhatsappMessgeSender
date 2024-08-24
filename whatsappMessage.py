import pyautogui
import time 
time.sleep(3)
for i in range(15):
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")