import os
import time


with open('host.txt') as file:
    dump = file.read().splitlines()

    for ip in dump:
        print('-' * 60)
        os.system(f'ping -c 2 {ip}')
        time.sleep(5)