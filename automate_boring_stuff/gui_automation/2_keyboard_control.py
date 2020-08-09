import pyautogui

pyautogui.hotkey('command', '?')
pyautogui.typewrite("Hello World!", interval=0.2)  # 0.2 sec pause in each character
pyautogui.typewrite(['backspace', 'left', 'left', 'X', 'Y'], interval=0.1)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.hotkey('command', 'd')

# https://automatetheboringstuff.com/chapter18/