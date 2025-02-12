import pyautogui
import time
import datetime
import random
import platform
from AppKit import NSApplication, NSApplicationActivationPolicyAccessory

# Initialize NSApp
app = NSApplication.sharedApplication()

# Hide the Dock icon
app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)

pyautogui.FAILSAFE = False
# Get current mouse location
screen_width, screen_height = pyautogui.size()
os_name = platform.system()
current_time = datetime.datetime.now()
current_day = current_time.strftime("%A")

def move_mouse(random_number):
    x, y = pyautogui.position()
    pyautogui.moveTo(x, y)
    time.sleep(random_number)

def otherDays():
    last_number = 0
    try:
        while True:
            last_random_number = random.randint(1, 5)
            random_number = random.randint(0, last_random_number)
            if last_number == random_number:
                pass
            else:
                move_mouse(random_number)
                last_number = random_number
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}")
        return

otherDays()
