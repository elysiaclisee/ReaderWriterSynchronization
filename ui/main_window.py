import threading
import tkinter as tk

from tkinter import ttk

from ui.control_panel import ControlPanel
from ui.activity_panel import ActivityPanel
from ui.log_panel import LogPanel
from ui.metrics_panel import MetricsPanel

class MainWindow(tk.Tk):

    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title("Reader Writer Simulator")
        self.geometry("1000x700")
        self.control_panel = ControlPanel(self,self.start_simulation)
        self.control_panel.pack(fill="x",padx=10,pady=5)
        self.activity_panel = ActivityPanel(self)

        self.activity_panel.pack(fill="x", padx=10, pady=5)
        self.log_panel = LogPanel(self)
        self.log_panel.pack(fill = "both",expand = True, padx=10, pady=5)   
        self.metrics_panel = MetricsPanel(self)
        self.metrics_panel.pack(fill="x", padx=10, pady=5)  
        self.after(200,self.refresh_ui)
    def start_simulation(self,policy,readers,writers):
        simulation_thread = threading.Thread(
            target=self.run_simulation,
            args=(policy, readers, writers)
        )
        simulation_thread.daemon = True
        simulation_thread.start()

    def run_simulation(self, policy,readers,writers):
        self.controller.launch_run(policy,readers,writers)
        self.controller.wait_until_finished()
    def refresh_ui(self):
        self.activity_panel.refresh(self.controller.runtime_state)
        self.log_panel.refresh(self.controller.runtime_state)
        self.metrics_panel.refresh(self.controller)
        self.after(200,self.refresh_ui)