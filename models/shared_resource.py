import threading

class SharedResource:
    def __init__(self):
        self.resource_value = 0
        self.value_guard = threading.Lock()
    def read(self):
        with self.value_guard:
            return self.resource_value
    def update(self):
        with self.value_guard:
            self.resource_value += 10
            return self.resource_value