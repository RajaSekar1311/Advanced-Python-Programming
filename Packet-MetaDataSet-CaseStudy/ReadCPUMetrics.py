import os
import psutil

processID = os.getpid()


python = psutil.Process(processID)

processName = psutil.Process.name(processID)

memoryUse = python.memory_info()[0]/2.**30
print('Process ID:',processID)
print('Process Name:',processName)
print('Memory use: ',memoryUse)