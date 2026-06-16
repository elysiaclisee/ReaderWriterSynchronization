import time
class Benchmark:
    def __init__(self):
        self.start_timestamp = None
        self.end_timestamp = None
    def start(self):
        self.start_timestamp = time.time()
    def stop(self):
        self.end_timestamp = time.time()

    @property
    def elapsed_time(self):
        if self.start_timestamp is None:
            return 0
        if self.end_timestamp is None:
            return 0
        return self.end_timestamp - self.start_timestamp
    def throughput(
        self,
        completed_tasks
    ):
        duration = self.elapsed_time
        if duration <= 0:
            return 0
        return completed_tasks / duration