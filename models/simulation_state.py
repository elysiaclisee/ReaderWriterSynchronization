import threading
class SimulationState:
    def __init__(self):
        self.pending_pool = [] # threads waiting for resource access
        self.reading_pool = []  # threads currently reading
        self.writing_pool = []  # threads currently writing
        self.resource_mode = "FREE" # FREE/READING/WRITING
        self.event_history = []  #event log displayed
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
            self.resource_mode = "READING" #resource is currently being read
    def remove_reader(self, thread_name):
        with self.lock:
            if thread_name in self.reading_pool:
                self.reading_pool.remove(thread_name)
            if (len(self.reading_pool) == 0 and len(self.writing_pool) == 0): # no active readers or writers remains
                self.resource_mode = "FREE"
    def add_writer(self, thread_name):
        with self.lock:
            self.writing_pool.clear()
            self.writing_pool.append(thread_name)
            self.resource_mode = "WRITING" #resource is currently being written
    def remove_writer(self, thread_name):
        with self.lock:
            if thread_name in self.writing_pool:
                self.writing_pool.remove(thread_name)
            if (len(self.reading_pool) == 0 and len(self.writing_pool) == 0):
                self.resource_mode = "FREE"
    def task_completed(self):
        with self.lock:
            self.completed_tasks += 1