import random
import threading
import time

class WriterThread(threading.Thread):

    def __init__(self,worker_id,access_policy,shared_resource,runtime_state):
        super().__init__()
        self.worker_id = worker_id
        self.access_policy = access_policy
        self.shared_resource = shared_resource
        self.runtime_state = runtime_state

    def run(self):

        self.runtime_state.append_log(f"{self.worker_id} arrived")         # Writer request arrives
        time.sleep(random.uniform(0.1, 1.5))
        self.access_policy.acquire_write(self.worker_id)        # Request exclusive write permission
        self.shared_resource.update()  #critical section
        time.sleep(random.uniform(1.0, 3.0))
        self.access_policy.release_write(self.worker_id) #release resource