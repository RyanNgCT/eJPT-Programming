import socket

target = input("Please enter target IP address to scan: ")
port_range = input("Please enter port range to scan: ")

lowport = int(port_range.split('-')[0])
highport = int(port_range.split('-')[1])

print(f"Scanning target IP {target}, from port {lowport} to port {highport}...")

for port in range(lowport,highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = s.connect_ex((target, port))
    if (res == 0):
        print(f"Port {port} is open.")
    
s.close()
