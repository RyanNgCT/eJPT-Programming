import socket
from datetime import datetime

HOST = '127.0.0.1' # or localhost
host = socket.gethostbyname(socket.gethostname())
PORT = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen() # if no. is specified, reject new connections after no.

now = datetime.now()

while True:
    # comms socket
    commsock, addr = s.accept()
    print(f'connected to {addr}')
    message = commsock.recv(1024).decode('utf-8')
    print(f'message from client is {message}')
    commsock.send('Message received at {}'.format(now.strftime("%H:%M:%S")).encode('utf-8'))
    commsock.close

print(host)
