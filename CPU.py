from datetime import *

import platform
import psutil
import time


class cpu:

    def __init__(self):
        # init
        self.system = None
        self.ramInfo = None

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
