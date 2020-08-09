import pyautogui
import os

# In linux "apt-get install scrot"
pyautogui.screenshot()  # Returns a pillow object
pyautogui.screenshot(f"{os.getenv('HOME')}/Downloads/examples.png")

print("********** Image recognition **********")
location = pyautogui.locateOnScreen(f"{os.getenv('HOME')}/Downloads/iterm_logo.png")
print(f"iterm_logo location={location}")  # Where on the screen it's able to find the iterm_logo
# x,y,width,height

location = pyautogui.locateCenterOnScreen(f"{os.getenv('HOME')}/Downloads/iterm_logo.png")
print(f"iterm_logo center location={location}")  # center of the iterm_logo
pyautogui.moveTo((103, 9), duration=1)
