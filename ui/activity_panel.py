import tkinter as tk
from tkinter import ttk

class ActivityPanel(ttk.LabelFrame):

    def __init__(self,parent):

        super().__init__(parent,text="Resource Visualization",padding=10)
        self.status_label = ttk.Label(self,text="FREE",font=("Arial", 12, "bold"))
        self.status_label.pack(pady=5)

        self.waiting_label = ttk.Label(self,text="Waiting Queue:")
        self.waiting_label.pack(anchor="w")
        self.reader_label = ttk.Label(self,text="Active Readers:")
        self.reader_label.pack(anchor="w")
        self.writer_label = ttk.Label(self,text="Active Writer:")
        self.writer_label.pack(anchor="w")

    def refresh(self, runtime_state):
        self.status_label.config(text=runtime_state.resource_mode)
        if runtime_state.resource_mode == "READING":
            self.status_label.config(foreground="green")
        elif runtime_state.resource_mode == "WRITING":
            self.status_label.config(foreground="red")
        else:
            self.status_label.config(foreground="blue")
        self.waiting_label.config(text="Waiting Queue: "+ ", ".join(runtime_state.pending_pool))
        self.reader_label.config(text="Active Readers: "+ ", ".join(runtime_state.reading_pool))
        self.writer_label.config(text="Active Writer: "+ ", ".join(runtime_state.writing_pool))