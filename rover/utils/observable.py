class Observable(object):
    def __init__(self):
        self._callbacks = []

    def attach(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def notify(self, modifier=None):
        for callback in self._callbacks:
            if modifier != callback:
                callback(self)
