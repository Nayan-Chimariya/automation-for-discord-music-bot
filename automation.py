import pyautogui
import time
from scrap_title import title
from image_processing import screenshot, ocr

url =""
n=0

def switch_window():
  pyautogui.keyDown('alt')
  time.sleep(.2)
  pyautogui.press('tab')
  pyautogui.press('enter')

def main():
  global n
  global url
  time.sleep(5)
  while n<30:
    name = title(url)
    switch_window()
    pyautogui.typewrite('/play')
    pyautogui.press('tab')
    pyautogui.typewrite(name)
    pyautogui.press('enter')
    switch_window()
    pyautogui.keyDown('shift')
    pyautogui.press('n')
    screenshot()
    url = ocr()
    n+=1

main()













