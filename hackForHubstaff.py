import pyautogui
import time
import random

print("program start in 5 sec")
time.sleep(10)

msg=["for ribbon in ordersInCart :","t=int(input('enter the times in number :- '))","<div class='container' data-aos='fade-up'>"]
random_msg = random.choice(msg)
sum =0

while(True):
    for key in random_msg:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)

    pyautogui.hotkey('ctrl', 'tab')

    for key in random_msg:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)

    time.sleep(5)
    pyautogui.hotkey('ctrl', 'tab')

    for _ in range(0,len(random_msg)):
        pyautogui.press('backspace')

    pyautogui.hotkey('ctrl', 'tab')

    for _ in range(0,len(random_msg)):
        pyautogui.press('backspace')
    sum = sum +5
    if(sum == 2400):
        break

