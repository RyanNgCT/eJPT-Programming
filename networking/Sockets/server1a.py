import socket

# internet socket (not unix) and TCP socket (not udp -> SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 13337))

s.listen()


while True:
    # accept every single client
    client, address = s.accept()
    print(f"Connected to {address}")
    client.send("You are connected!".encode())

    client.close()
    
