import random
import threading
import time


class ReaderThread(threading.Thread):

    def __init__(self,worker_id,access_policy,shared_resource,runtime_state):
        super().__init__()
        self.worker_id = worker_id
        self.access_policy = access_policy
        self.shared_resource = shared_resource
        self.runtime_state = runtime_state
    def run(self):
        self.runtime_state.append_log(f"{self.worker_id} arrived")  # reader request arrived
        time.sleep(random.uniform(0.1, 1.5)) #simulated arrival delay
        self.access_policy.acquire_read(self.worker_id) #request read permission
        _ = self.shared_resource.read() #critical section

        time.sleep(random.uniform(1.0, 3.0))  #simulated reading time
        self.access_policy.release_read(self.worker_id) # release resource