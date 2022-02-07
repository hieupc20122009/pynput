The listener callbacks are invoked directly from an operating thread on some platforms, notably Windows.
This means that long running procedures and blocking operations should not be invoked from the callback, as this risks freezing input for all processes.
A possible workaround is to just dispatch incoming messages to a queue, and let a separate thread handle them.
