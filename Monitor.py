from functions.py import  *
import win32api, time

def printInfo(device):
    print((device.DeviceName, device.DeviceString))
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    for info in ['Color', 'BitsPerPel', 'DisplayFrequency']:
        print("%s: %s"%(info, getattr(settings, info)))



while True:
    device = win32api.EnumDisplayDevices()
   # for loop in ['1', '2', '3', '4']:
   #     print(f"\n")
    printInfo(device)
    time.sleep(5)