from tkinter import ttk
import tkinter as tk
class LogPanel(ttk.LabelFrame):
    def __init__(self,parent):
        super().__init__(parent,text="Live Event Log",padding=10)
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        self.log_scrollbar = ttk.Scrollbar(container, orient="vertical")
        self.log_scrollbar.pack(side="right", fill="y")

        self.log_box = tk.Text(container, height=10, width=60, yscrollcommand=self.log_scrollbar.set)
        self.log_box.pack(side="left", fill="both", expand=True)
        self.log_scrollbar.config(command=self.log_box.yview)
        self.log_box.config(state="disabled")
    def refresh(self,runtime_state):
        first_visible, last_visible = self.log_box.yview()
        follow_latest = last_visible >= 0.999
        self.log_box.config(state="normal")
        self.log_box.delete("1.0",tk.END)
        for item in runtime_state.event_history:
            self.log_box.insert(tk.END,item + "\n")
        if follow_latest:
            self.log_box.see(tk.END)
        else:
            self.log_box.yview_moveto(first_visible)
        self.log_box.config(state="disabled")