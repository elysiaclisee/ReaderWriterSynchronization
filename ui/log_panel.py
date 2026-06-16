from tkinter import ttk
import tkinter as tk
class LogPanel(ttk.LabelFrame):
    def __init__(self,parent):
        super().__init__(parent,text="Live Event Log",padding=10)
        self.log_box = tk.Text(self,height=15,width=60)
        self.log_box.pack(fill="both",expand=True)
        self.log_box.config(state="disabled")
    def refresh(self,runtime_state):
        self.log_box.config(state="normal")
        self.log_box.delete("1.0",tk.END)
        for item in runtime_state.event_history:
            self.log_box.insert(tk.END,item + "\n")
        self.log_box.see(tk.END)
        self.log_box.config(state="disabled")