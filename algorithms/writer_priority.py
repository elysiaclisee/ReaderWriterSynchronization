import threading
from algorithms.base import AccessPolicy

class WriterPriority(AccessPolicy):
    def __init__(self, runtime_state):
        super().__init__(runtime_state)
        self.active_reader_total = 0
        self.queued_writer_total = 0
        self.reader_counter_guard = threading.Lock()
        self.writer_counter_guard = threading.Lock()
        self.entry_gate = threading.Semaphore(1)
        self.resource_token = threading.Semaphore(1)
    def acquire_read(self, thread_name):
        self.runtime_state.add_waiting(thread_name)
        self.entry_gate.acquire()
        self.entry_gate.release()
        with self.reader_counter_guard:
            self.active_reader_total += 1
            if self.active_reader_total == 1:
                self.resource_token.acquire()
        self.runtime_state.remove_waiting(thread_name)
        self.runtime_state.add_reader(thread_name)
        self.runtime_state.append_log(f"{thread_name} started reading")
    def release_read(self, thread_name):
        with self.reader_counter_guard:
            self.active_reader_total -= 1
            if self.active_reader_total == 0:
                self.resource_token.release()
        self.runtime_state.remove_reader(thread_name)
        self.runtime_state.task_completed()
        self.runtime_state.append_log(f"{thread_name} finished reading")
    def acquire_write(self, thread_name):
        self.runtime_state.add_waiting(thread_name)
        with self.writer_counter_guard:
            self.queued_writer_total += 1
            if self.queued_writer_total == 1:
                self.entry_gate.acquire()
        self.resource_token.acquire()
        self.runtime_state.remove_waiting(thread_name)
        self.runtime_state.add_writer(thread_name)
        self.runtime_state.append_log(f"{thread_name} started writing")
    def release_write(self, thread_name):
        self.runtime_state.remove_writer(thread_name)
        self.resource_token.release()
        with self.writer_counter_guard:
            self.queued_writer_total -= 1
            if self.queued_writer_total == 0:
                self.entry_gate.release()
        self.runtime_state.task_completed()
        self.runtime_state.append_log(f"{thread_name} finished writing")