import pyautogui
import time

while True:
  pyautogui.moveRel(8, -8)
  time.sleep(1)
  pyautogui.moveRel(-8, 8)
  time.sleep(1)
