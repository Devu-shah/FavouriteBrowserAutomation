import pyautogui
# from time import sleep
from pyautogui import time
import os

def runner():
    browser_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

    os.startfile(browser_path)

    site = 'https://www.google.co.in'

    time.sleep(6.0)
    
    for word in site:
        pyautogui.typewrite(word)
        pyautogui.press('enter')


try:
    pass
except Exception as e:
    print(Exception)
runner()