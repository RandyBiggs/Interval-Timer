import tkinter as tk
import os

counter = 300


def format_time(c):
    mins = int(c / 60)
    secs = c - mins * 60
    return str(mins) + ":" + "%02d" % secs


def update_counter(label):
    def count():
        global counter
        if counter == 240:
            os.system('afplay /System/Library/Sounds/pop.aiff')
        if counter == 180:
            os.system('afplay /System/Library/Sounds/pop.aiff')
        if counter == 120:
            os.system('afplay /System/Library/Sounds/pop.aiff')
        if counter == 60:
            os.system('afplay /System/Library/Sounds/pop.aiff')
        if counter == 3:
            os.system('afplay /System/Library/Sounds/ping.aiff')
        if counter == 2:
            os.system('afplay /System/Library/Sounds/ping.aiff')
        if counter == 1:
            os.system('afplay /System/Library/Sounds/ping.aiff')
        if counter == 0:
            reset_counter(label)
            os.system('afplay /System/Library/Sounds/glass.aiff')
        counter -= 1
        f_time = format_time(counter)
        label.config(text=str(f_time))
        label.after(1000, count)

    count()


def reset_counter(label):
    global counter
    counter = 300
    f_time = format_time(counter)
    label.config(text=str(f_time))


increment = 1
settings_open = False


class CounterGUI:
    global counter

    def __init__(self):
        self.__mainwindow = tk.Tk()
        self.__mainwindow.title("Interval Timer")
        self.cLabel = tk.Label(text=format_time(counter), height=3)
        self.cLabel.grid(row=0, column=1, sticky='WE')
        update_counter(self.cLabel)
        self.pButton = tk.Button(self.__mainwindow, text="+", width=5, height=2)
        self.pButton.grid(row=3, column=2, sticky='E')
        self.pButton.bind('<Button-1>', self.pCounter)
        self.mButton = tk.Button(self.__mainwindow, text="-", width=5, height=2)
        self.mButton.grid(row=3, column=0, sticky='E')
        self.mButton.bind("<Button-1>", self.mCounter)
        self.rButton = tk.Button(self.__mainwindow, text="Reset", width=20, height=2)
        self.rButton.grid(row=3, column=1, sticky='E')
        self.rButton.bind("<Button-1>", self.rCounter)
        self.sButton = tk.Button(self.__mainwindow, text="*", width=2, height=1)
        self.sButton.grid(row=0, column=2)
        self.sButton.bind("<Button-1>", self.toggle_settings)
        self.incEntry = tk.Entry(self.__mainwindow, width=15)
        self.incEntry.bind("<Return>", self.setIncrement, self.toggle_settings)
        self.__mainwindow.after_idle(self.__mainwindow.call, 'wm', 'attributes', '.', '-topmost', True)
        self.__mainwindow.mainloop()

    def pCounter(self, event):
        global counter
        global increment
        counter += increment
        f_time = format_time(counter)
        self.cLabel.config(text=str(f_time))

    def mCounter(self, event):
        global counter
        global increment
        counter -= increment
        f_time = format_time(counter)
        self.cLabel.config(text=str(f_time))

    def rCounter(self, event):
        global counter
        global increment
        counter = 300
        f_time = format_time(counter)
        self.cLabel.config(text=str(f_time))
        os.system('afplay /System/Library/Sounds/Bottle.aiff')

    def toggle_settings(self, event):
        global settings_open
        if not settings_open:
            self.incEntry.grid(row=2, column=1, sticky='WE')
            self.incLabel = tk.Label(self.__mainwindow, text="Set Increment:")
            self.incLabel.grid(row=1, column=1, sticky='WE')
            settings_open = True
        else:
            self.incEntry.grid_remove()
            self.incLabel.grid_remove()
            settings_open = False

    def setIncrement(self, event):
        global increment
        increment = int(self.incEntry.get())
        self.incEntry.grid_remove()
        self.incLabel.grid_remove()


gui = CounterGUI()
