import tkinter as tk
from tkinter import ttk


class ControlPanel(ttk.LabelFrame):
    def __init__(self,parent,start_callback):
        super().__init__(parent,text="Control Panel",padding=10)
        self.start_callback = start_callback
        ttk.Label(self, text="Scheduling Policy").grid(row=0,column=0,sticky="w",padx=5,pady=5)
        self.policy_selector = ttk.Combobox(self,state="readonly",values=["Reader Priority","Writer Priority","FCFS Fairness"]) 
        self.policy_selector.current(0)
        self.policy_selector.grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(self,text="Readers").grid(row=1,column=0,sticky="w",padx=5,pady=5)
        self.reader_input = ttk.Entry(self,width=10)
        self.reader_input.insert(0,"10")
        self.reader_input.grid(row=1,column=1,padx=5,pady=5)
        ttk.Label(self,text="Writers").grid(row=2,column=0,sticky="w",padx=5,pady=5)
        self.writer_input = ttk.Entry(self,width=10)
        self.writer_input.insert(0,"5")
        self.writer_input.grid(row=2,column=1,padx=5,pady=5)
        self.run_button = ttk.Button(self,text="RUN",command=self.launch)
        self.run_button.grid(row=3,column=0,columnspan=2,pady=10)
    def launch(self):
        self.start_callback(
            self.policy_selector.get(),
            int(self.reader_input.get()),
            int(self.writer_input.get())
        )