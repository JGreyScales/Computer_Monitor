import psutil
import platform


class disk:

    def __init__(self):
        # init
        self.disk1Info = None

    def disk1(self):
        # gathers info on disks
        partitions = psutil.disk_partitions()
        disk_io = psutil.disk_io_counters()
        self.disk1Info = {
            "partitions": partitions,
            "disk_io": disk_io
        }
        return self.disk1Info
