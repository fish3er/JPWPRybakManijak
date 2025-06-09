import psutil
import os

def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / 1024 ** 2  # RSS in MB
    return round(mem, 2)



print('Memory before: {} MB'.format(memory_usage_psutil()))

