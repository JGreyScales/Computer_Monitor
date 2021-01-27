import psutil
import platform
from datetime import datetime


class network:
    def __init__(self):
        # init
        self.array = None

    def getnetwork(self):
        # gathers info on the network
        addrs = psutil.net_if_addrs()
        net = psutil.net_io_counters()
        self.array = [addrs, net.bytes_sent, net.bytes_recv]
        return self.array
