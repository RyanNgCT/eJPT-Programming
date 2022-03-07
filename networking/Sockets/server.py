import socket
import threading

PORT = 31337

# similar to Windows API function
SERVER = socket.gethostbyname(socket.gethostname())

print(SERVER)

