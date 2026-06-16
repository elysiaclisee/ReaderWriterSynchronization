import threading

class SharedResource:
    def __init__(self):
        self.resource_value = 0 #shared data 
        self.value_guard = threading.Lock() #resource lock
    def read(self):
        with self.value_guard: # critical section for reading
            return self.resource_value
    def update(self): 
        with self.value_guard: # critical section for writing
            self.resource_value += 10
            return self.resource_value