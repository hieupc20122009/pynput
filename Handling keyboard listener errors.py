If a callback handler raises an exception, the listener will be stopped. Since callbacks run in a dedicated thread, the exceptions will not automatically be reraised.
To be notified about callback errors, call Thread.join on the listener instance:

from pynput import keyboard

class MyException(Exception): pass

def on_press(key):
    if key == keyboard.Key.esc:
        raise MyException(key)

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
