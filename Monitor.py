from screeninfo import *

import time
import win32api
import wmi


class monitorInfo:

    def __init__(self):
        # init function
        self.fullInfo = None
        self.displays = None
        self.monitors = None
        self.displayInfo = None

    def gatherInfo(self):
        # gathers the info for the monitors and puts it into vars
        device = win32api.EnumDisplayDevices()
        obj = wmi.WMI().Win32_PnPEntity(ConfigManagerErrorCode=0)
        self.displays = [x for x in obj if 'DISPLAY' in str(x)]
        self.monitors = get_monitors()
        self.displayInfo = win32api.EnumDisplaySettings(device.DeviceName, 0)
        self.fullInfo = [self.displayInfo, self.monitors, self.displayInfo]

        return self.fullInfo
