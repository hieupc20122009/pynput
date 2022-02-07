Once pynput.mouse.Listener.stop has been called, the listener cannot be restarted, since listeners are instances of threading.Thread.
If your application requires toggling listening events, you must either add an internal flag to ignore events when not required, or create a new listener when resuming listening
