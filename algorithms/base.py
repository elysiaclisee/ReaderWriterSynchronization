from abc import ABC, abstractmethod
class AccessPolicy(ABC):
    def __init__(self, runtime_state):
        self.runtime_state = runtime_state

    @abstractmethod
    def acquire_read(self, thread_name):
        pass

    @abstractmethod
    def release_read(self, thread_name):
        pass

    @abstractmethod
    def acquire_write(self, thread_name):
        pass

    @abstractmethod
    def release_write(self, thread_name):
        pass