import threading
from algorithms.base import AccessPolicy

class ReaderPriority(AccessPolicy):

    def __init__(self, runtime_state):

        super().__init__(runtime_state)
        self.reader_total = 0                     #number of active readers
        self.counter_guard = threading.Lock()
        self.access_token = threading.Semaphore(1) #shared resource lock

    def acquire_read(self, thread_name):

        self.runtime_state.add_waiting(thread_name)
        with self.counter_guard:
            self.reader_total += 1
            if self.reader_total == 1: #first reader blocks writers
                self.access_token.acquire()
        self.runtime_state.remove_waiting(thread_name)
        self.runtime_state.add_reader(thread_name)
        self.runtime_state.append_log(f"{thread_name} started reading")

    def release_read(self, thread_name):

        with self.counter_guard:
            self.reader_total -= 1
            if self.reader_total == 0: #last reader allows writers to proceed
                self.access_token.release()
        self.runtime_state.remove_reader(thread_name)
        self.runtime_state.task_completed()
        self.runtime_state.append_log(f"{thread_name} finished reading")

    def acquire_write(self, thread_name):

        self.runtime_state.add_waiting(thread_name)
        self.access_token.acquire()  #writer must wait until all readers leave
        self.runtime_state.remove_waiting(thread_name)
        self.runtime_state.add_writer(thread_name)
        self.runtime_state.append_log(f"{thread_name} started writing")

    def release_write(self, thread_name):

        self.runtime_state.remove_writer(thread_name)
        self.access_token.release() # release resource for next reader
        self.runtime_state.task_completed()
        self.runtime_state.append_log(f"{thread_name} finished writing")