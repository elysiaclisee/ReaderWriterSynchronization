import threading
from algorithms.base import AccessPolicy
class FairnessFCFS(AccessPolicy):
    def __init__(self, runtime_state):
        super().__init__(runtime_state)
        self.reader_group_size = 0
        self.arrival_turnstile = threading.Semaphore(1)
        self.resource_token = threading.Semaphore(1)
        self.counter_guard = threading.Lock()
    def acquire_read(self, thread_name):
        self.runtime_state.add_waiting(thread_name)
        self.arrival_turnstile.acquire()
        with self.counter_guard:
            self.reader_group_size += 1
            if self.reader_group_size == 1:
                self.resource_token.acquire()
        self.arrival_turnstile.release()
        self.runtime_state.remove_waiting(thread_name)
        self.runtime_state.add_reader(thread_name)
        self.runtime_state.append_log(f"{thread_name} started reading")
    def release_read(self, thread_name):
        with self.counter_guard:
            self.reader_group_size -= 1
            if self.reader_group_size == 0:
                self.resource_token.release()
        self.runtime_state.remove_reader(thread_name)
        self.runtime_state.task_completed()
        self.runtime_state.append_log(f"{thread_name} finished reading")
    def acquire_write(self, thread_name):
        self.runtime_state.add_waiting(thread_name)
        self.arrival_turnstile.acquire()
        self.resource_token.acquire()
        self.arrival_turnstile.release()
        self.runtime_state.remove_waiting(thread_name)
        self.runtime_state.add_writer(thread_name)
        self.runtime_state.append_log(f"{thread_name} started writing")
    def release_write(self, thread_name):
        self.runtime_state.remove_writer(thread_name)
        self.resource_token.release()
        self.runtime_state.task_completed()
        self.runtime_state.append_log(f"{thread_name} finished writing")