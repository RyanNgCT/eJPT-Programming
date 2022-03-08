## TCP Port Scanner

import socket
import threading
from queue import Queue


#target = "192.168.233.196"
target = "127.0.0.1"
queue = Queue()
open_ports = []

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

"""for i in range(1,65535):
    result = portscan(i)
    if result:
        print(f"Port {i} is open")"""

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"Port {port} is open\n")
            open_ports.append(port)


port_list = range(1,65535)
fill_queue(port_list)
thread_list = []
for i in range(1000):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()

print(thread_list)
print("Open ports are: ", open_ports)
            

    

