import threading
from algorithms.base import AccessPolicy

class FairnessFCFS(AccessPolicy):
    
    def __init__(self, runtime_state):

        super().__init__(runtime_state)
        self.reader_group_size = 0                 # Number of readers currently sharing the resource
        self.arrival_turnstile = threading.Semaphore(1) #Arrival queue (turnstile) to preserve FCFS ordering
        self.resource_token = threading.Semaphore(1)  #Token to control access to the shared resource
        self.counter_guard = threading.Lock() #Protect reader counter updates
    
    def acquire_read(self, thread_name):

        self.runtime_state.add_waiting(thread_name)        # Reader arrives and joins waiting queue
        self.arrival_turnstile.acquire()        # Wait for its turn in arrival order
        with self.counter_guard:
            self.reader_group_size += 1
            if self.reader_group_size == 1:             # First reader locks the shared resource
                self.resource_token.acquire()
        self.arrival_turnstile.release()        # Allow next arriving request to proceed
        self.runtime_state.remove_waiting(thread_name)        # Reader enters critical section
        self.runtime_state.add_reader(thread_name)       
        self.runtime_state.append_log(f"{thread_name} started reading")

    def release_read(self, thread_name):

        with self.counter_guard:
            self.reader_group_size -= 1
            if self.reader_group_size == 0:
                self.resource_token.release()
        self.runtime_state.remove_reader(thread_name)         # Reader leaves critical section
        self.runtime_state.task_completed()
        self.runtime_state.append_log(f"{thread_name} finished reading")
    
    def acquire_write(self, thread_name):
        
        self.runtime_state.add_waiting(thread_name)          # Writer arrives and joins waiting queue
        self.arrival_turnstile.acquire()         # Wait in FCFS order
        self.resource_token.acquire()        # Writer requires exclusive ownership
        self.arrival_turnstile.release()        # Allow next request to enter the arrival queue
        self.runtime_state.remove_waiting(thread_name)        # Writer enters critical section
        self.runtime_state.add_writer(thread_name)
        self.runtime_state.append_log(f"{thread_name} started writing")
    
    def release_write(self, thread_name):

        self.runtime_state.remove_writer(thread_name)       # Writer releases exclusive ownership
        self.resource_token.release()
        self.runtime_state.task_completed()
        self.runtime_state.append_log(f"{thread_name} finished writing")