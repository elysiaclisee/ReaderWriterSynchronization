import random
from algorithms.reader_priority import ReaderPriority
from algorithms.writer_priority import WriterPriority
from algorithms.fairness_fcfs import FairnessFCFS

from threads.reader import ReaderThread
from threads.writer import WriterThread

from utils.benchmark import Benchmark

class SimulationController:

    def __init__(self,runtime_state,shared_resource):
        self.runtime_state = runtime_state
        self.shared_resource = shared_resource
        self.worker_pool = []
        self.benchmark = Benchmark()
        self.execution_time = 0
        self.processing_rate = 0
    def build_policy(self,policy_name):
        # Create synchronization policy selected by user
        if policy_name == "Reader Priority":
            return ReaderPriority(self.runtime_state)
            
        if policy_name == "Writer Priority":
            return WriterPriority(self.runtime_state)
        return FairnessFCFS(self.runtime_state)
    def reset_state(self): # Reset simulation state before starting a new run

        self.runtime_state.pending_pool.clear()

        self.runtime_state.reading_pool.clear()

        self.runtime_state.writing_pool.clear()

        self.runtime_state.event_history.clear()

        self.runtime_state.completed_tasks = 0

        self.runtime_state.resource_mode = "FREE"

        self.shared_resource.resource_value = 0

        self.worker_pool.clear()

    def build_workers(self,reader_count,writer_count,policy):
        for idx in range(reader_count):        # Create reader threads
            reader = ReaderThread(
                worker_id=f"R - {idx + 1}",
                access_policy=policy,
                shared_resource=self.shared_resource,
                runtime_state=self.runtime_state
            )
            self.worker_pool.append(reader)
        for idx in range(writer_count):        # Create writer threads
            writer = WriterThread(
                worker_id=f"W - {idx + 1}",
                access_policy=policy,
                shared_resource=self.shared_resource,
                runtime_state=self.runtime_state
            )
            self.worker_pool.append(writer)
        random.shuffle(self.worker_pool)         # Randomize arrival order for simulation

    def launch_run(self,policy_name,reader_count,writer_count):
        self.reset_state()
        policy = self.build_policy(policy_name)
        self.build_workers(reader_count,writer_count,policy)
        self.benchmark.start()        # Start performance measurement
        for worker in self.worker_pool:   # Launch all worker threads
            worker.start()
    def wait_until_finished(self):
        # Wait for all threads to complete
        for worker in self.worker_pool:
            worker.join()
        self.benchmark.stop()
        self.finalize_statistics()
    def finalize_statistics(self):
        # Calculate final performance metrics
        self.execution_time = round(self.benchmark.elapsed_time,2)

        self.processing_rate = round(self.benchmark.throughput(self.runtime_state.completed_tasks),2)