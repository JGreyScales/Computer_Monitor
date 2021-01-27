import GPUtil
from tabulate import tabulate

class gpu:

    def __init__(self):
        self.array = None

    def gpu(self):
        gpus = GPUtil.getGPUs()
        self.array = []
        for gpu1 in gpus:
            # get the GPU id
            gpu_id = gpu1.id
            # name of GPU
            gpu_name = gpu1.name
            # get % percentage of GPU usage of that GPU
            gpu_load = f"{gpu1.load * 100}%"
            # get free memory in MB format
            gpu_free_memory = f"{gpu1.memoryFree}MB"
            # get used memory
            gpu_used_memory = f"{gpu1.memoryUsed}MB"
            # get total memory
            gpu_total_memory = f"{gpu1.memoryTotal}MB"
            # get GPU temperature in Celsius
            gpu_temperature = f"{gpu1.temperature} °C"
            gpu_uuid = gpu1.uuid
            self.array.append((
                gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                gpu_total_memory, gpu_temperature, gpu_uuid
            ))
        return self.array
