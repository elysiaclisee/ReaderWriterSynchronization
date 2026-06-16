from tkinter import ttk
class MetricsPanel(ttk.LabelFrame):
    def __init__(self,parent):
        super().__init__(parent,text="Performance",padding=10)
        self.time_label = ttk.Label(self,text="Execution Time: 0")
        self.time_label.pack(anchor="w")
        self.rate_label = ttk.Label(self,text="Throughput: 0")
        self.rate_label.pack(anchor="w")
        self.task_label = ttk.Label(self,text="Completed Tasks: 0")
        self.task_label.pack(anchor="w")
        self.value_label = ttk.Label(self,text="Resource Value: 0")
        self.value_label.pack(anchor="w")
    def refresh(self,controller):
        self.time_label.config(text=f"Execution Time: {controller.execution_time}s")
        self.rate_label.config(text=f"Throughput: {controller.processing_rate}")
        self.task_label.config(text=f"Completed Tasks: " f"{controller.runtime_state.completed_tasks}")
        self.value_label.config(text=f"Resource Value: " f"{controller.shared_resource.resource_value}")