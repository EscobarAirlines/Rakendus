import os
import sys
import pyowm 
import psutil
import platform
from pyowm.owm import OWM
from datetime import datetime

BYTE_TO_MEGABYTE = 0.00000095367432

city = 'Tallinn'
owm = OWM('API KEY')
manager = owm.weather_manager()
observation = manager.weather_at_place(city)
weather = observation.weather


memory = psutil.virtual_memory()
memory_total = getattr(memory, 'total') * BYTE_TO_MEGABYTE
memory_free = getattr(memory, 'free') * BYTE_TO_MEGABYTE
memory_used = getattr(memory, 'used') 
memory_limit = (memory_used / 100 * 20) * BYTE_TO_MEGABYTE


disk = psutil.disk_usage('/')
disk_free = getattr(disk, 'total') * BYTE_TO_MEGABYTE
disk_total = getattr(disk, 'free') * BYTE_TO_MEGABYTE
disk_used = getattr(disk, 'used') 
disk_limit = (disk_used / 100 * 20) * BYTE_TO_MEGABYTE


def memory_info():
    print('RAM:')
    print('Your total memory: ', round(memory_total, 2), 'MB')
    print('Memory available: ', round(memory_free, 2), 'MB')


def disk_info():
    print('\nDisk usage:')
    print('Your total disk memory: ', round(disk_free, 2), 'MB')
    print('Disk memory available: ', round(disk_total, 2), 'MB')
    
    
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


memory_info()
disk_info()


if memory_used > memory_limit:
    print('WARNING: Stop this, you are using more than 20% of memory!!!!')
elif disk_used > disk_limit:
    print('WARNING: Stop this, you are using more than 20% of disk!!!!!')


input()


with open('history.txt', mode='a')as history:
    current_time = str(datetime.now()) 

    history.write(current_time)
    history.write(str(weather))
    history.write('\nRAM:\n')
    history.write(str(round(memory_total, 2)))
    history.write('\n')
    history.write(str(round(memory_free, 2)))
    history.write('\n')

    history.write('\ndisk:\n')
    history.write(str(round(disk_free, 2)))
    history.write('\n')
    history.write(str(round(disk_total, 2)))
    history.write('\n\n')

    history.close()