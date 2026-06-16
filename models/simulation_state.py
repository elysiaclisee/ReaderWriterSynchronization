import threading
class SimulationState:
    def __init__(self):
        self.pending_pool = []
        self.reading_pool = []
        self.writing_pool = []
        self.resource_mode = "FREE"
        self.event_history = []
        self.completed_tasks = 0
        self.lock = threading.Lock()
    def append_log(self, message):
        with self.lock:
            self.event_history.append(message)
            if len(self.event_history) > 200:
                self.event_history.pop(0)
    def add_waiting(self, thread_name):
        with self.lock:
            if thread_name not in self.pending_pool:
                self.pending_pool.append(thread_name)

    def remove_waiting(self, thread_name):
        with self.lock:
            if thread_name in self.pending_pool:
                self.pending_pool.remove(thread_name)
    def add_reader(self, thread_name):
        with self.lock:
            if thread_name not in self.reading_pool:
                self.reading_pool.append(thread_name)
            self.resource_mode = "READING"
    def remove_reader(self, thread_name):
        with self.lock:
            if thread_name in self.reading_pool:
                self.reading_pool.remove(thread_name)
            if (len(self.reading_pool) == 0 and len(self.writing_pool) == 0):
                self.resource_mode = "FREE"
    def add_writer(self, thread_name):
        with self.lock:
            self.writing_pool.clear()
            self.writing_pool.append(thread_name)
            self.resource_mode = "WRITING"
    def remove_writer(self, thread_name):
        with self.lock:
            if thread_name in self.writing_pool:
                self.writing_pool.remove(thread_name)
            if (len(self.reading_pool) == 0 and len(self.writing_pool) == 0):
                self.resource_mode = "FREE"
    def task_completed(self):
        with self.lock:
            self.completed_tasks += 1