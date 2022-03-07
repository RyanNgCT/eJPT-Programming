import socket

# internet socket (not unix) and TCP socket (not udp -> SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',13337))

msg = s.recv(1024)
s.close()

print(msg.decode())
