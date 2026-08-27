import platform
import shutil
import psutil
import socket


per_core = psutil.cpu_percent(interval=0.5, percpu=True)
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()



total, used, free = shutil.disk_usage("/")

my_system = platform.uname()


print(r"""  ___ ___ __  __ _____   ___    
 / __|_ _|  \/  | _ \ \ / / |   
 \__ \| || |\/| |  _/\ V /| |__ 
 |___/___|_|  |_|_|   |_| |____|
                                """)

print(f"Hostname:", socket.gethostname())
print(f"System: {my_system.system}")
print(f"Architecture:", platform.architecture()[0])
print(f"Processor: {my_system.processor}")
print(f"Total CPU usage:", psutil.cpu_percent(interval=None), "%")
print(f"Total Storage: %d GiB" % (total // (2**30)))
print(f"RAM usage:", svmem.percent, "%")

input("Press Enter to exit")

