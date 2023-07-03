import pyautogui


def takeSS():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'\screenshot_____1.png')