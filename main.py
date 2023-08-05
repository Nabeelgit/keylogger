from pynput.keyboard import Key, Listener
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if pressed:
        print(f"{button} pressed at {x},{y}")

def on_press(key):
    print(key)



from pynput import keyboard
key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()

with Listener(on_click=on_click) as listener:
    listener.join()