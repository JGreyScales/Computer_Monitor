from tkinter import *

import os
import time
import tkinter
import win32api
import wmi
from CPU import *
from DISKS import disk
from Monitor import monitorInfo
from NETWORK import network

window_main = tkinter.Tk(className='Task manager')
window_main.geometry("800x340")
window_main.configure(bg='grey')


class submit:

    def __init__(self):
        # init
        self.system = None
        self.ramInfo = None
        self.ram()
        self.cpuInfo()

    def cpuInfo(self):
        # gathers info on cpu
        bluntSystem = platform.uname()
        bootTime = psutil.boot_time()
        bootTimeFormatted = datetime.fromtimestamp(bootTime)
        self.system = [bluntSystem.system, bluntSystem.node, bluntSystem.release, bluntSystem.version,
                       bluntSystem.machine, bluntSystem.processor, bootTime, bootTimeFormatted]
        return self.system

    def ram(self):
        # gathers info on  ram
        vram = psutil.virtual_memory()
        swap = psutil.swap_memory()
        self.ramInfo = [vram, vram.available, vram.used, vram.percent, swap, swap.free, swap.used, swap.percent,
                        vram.total, swap.total]
        return self.ramInfo

    def displayram(self):
        # is the function for when CPU is clicked
        pass

    def displaydisk(self):
        # is the function for when DISKS is clicked
        print('DISKS clicked')

    def displaygpu(self):
        # is the function for when the GPU is clicked
        print('GPU clicked')

    def displaynonitor(self):
        # is the function for when the MONITOR is clicked
        print("MONITOR clicked")

    def displaynetwork(self):
        # is the function for when NETWORK is clicked
        print("NETWORK clicked")

    def displayprocesses(self):
        # is the function for when PROCESSES is clicked
        print("Processes clicked")


a = submit()
button = [a.displayram, a.displaydisk, a.displaygpu, a.displaynonitor, a.displaynetwork,
          a.displayprocesses]
y = 0
files = ["CPU", "DISKS", "GPU", "MONITOR", "NETWORK", "PROCESSES"]
# creates button
for item in range(len(files)):
    # creates the button and
    button_submit = tkinter.Button(window_main, text=files[item], command=button[item])
    button_submit.config(width=20, height=1, bg="gray83")
    button_submit.pack()
    button_submit.place(x=25, y=y)
    y = y + 24

# the application mainloop
window_main.mainloop()

print("y close")
