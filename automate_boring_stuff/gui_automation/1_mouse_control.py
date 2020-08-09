# (0,0) is the top left corner of the screen
import pyautogui

print(f"Screen resolution={pyautogui.size()}")
width, height = pyautogui.size()

print(f"Current coordinate of the mouse cursor={pyautogui.position()}")

pyautogui.moveTo(1440, 900)
pyautogui.moveTo(0, 500, duration=1.5)

# move relative to a position
pyautogui.moveRel(1000, 0, duration=1.5)  # move 1000 pixels to the right
pyautogui.moveRel(1, -100, duration=1.5)  # move 100 pixels up

# click on iTerm2
# position of iTerm2 link (x=74, y=9).
# You can get the position by keeping the mouse on iTerm2 and pyautogui.position()
pyautogui.click(74, 9)
pyautogui.doubleClick(74, 9)
pyautogui.rightClick(74, 9)
pyautogui.middleClick(74, 9)
# pyautogui.drag()
# pyautogui.dragTo()
# pyautogui.dragRel()

print("******* Get the coordinates of screen parts *******")
# python
# >> import pyautogui
# >> pyautogui.displayMousePosition()
pyautogui.displayMousePosition()
