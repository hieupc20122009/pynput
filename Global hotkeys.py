A common use case for keyboard monitors is reacting to global hotkeys. Since a listener does not maintain any state, hotkeys involving multiple keys must store this state somewhere.

pynput provides the class pynput.keyboard.HotKey for this purpose. It contains two methods to update the state, designed to be easily interoperable with a keyboard listener: pynput.keyboard.HotKey.press and pynput.keyboard.HotKey.release which can be directly passed as listener callbacks.

The intended usage is as follows:

from pynput import keyboard

def on_activate():
    print('Global hotkey activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
This will create a hotkey, and then use a listener to update its state. Once all the specified keys are pressed simultaneously, on_activate will be invoked.

Note that keys are passed through pynput.keyboard.Listener.canonical before being passed to the HotKey instance. This is to remove any modifier state from the key events, and to normalise modifiers with more than one physical button.

The method pynput.keyboard.HotKey.parse is a convenience function to transform shortcut strings to key collections. Please see its documentation for more information.

To register a number of global hotkeys, use the convenience class pynput.keyboard.GlobalHotKeys:

from pynput import keyboard

def on_activate_h():
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_h,
        '<ctrl>+<alt>+i': on_activate_i}) as h:
    h.join()
