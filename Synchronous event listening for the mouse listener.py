To simplify scripting, synchronous event listening is supported through the utility class pynput.mouse.Events. This class supports reading single events in a non-blocking fashion, as well as iterating over all events.

To read a single event, use the following code:

from pynput import mouse

# The event listener will be running in this block
with mouse.Events() as events:
    # Block at most one second
    event = events.get(1.0)
    if event is None:
        print('You did not interact with the mouse within one second')
    else:
        print('Received event {}'.format(event))
To iterate over mouse events, use the following code:

from pynput import mouse

# The event listener will be running in this block
with mouse.Events() as events:
    for event in events:
        if event.button == mouse.Button.right:
            break
        else:
            print('Received event {}'.format(event))
Please note that the iterator method does not support non-blocking operation, so it will wait for at least one mouse event.

The events will be instances of the inner classes found in pynput.mouse.Events.
