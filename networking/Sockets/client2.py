import socket

HOST = '127.0.0.1' # or localhost
PORT = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

s.send("Hello World!".encode('utf-8'))
print(s.recv(1024).decode('utf-8'))
