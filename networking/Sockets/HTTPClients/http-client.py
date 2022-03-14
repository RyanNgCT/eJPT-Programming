import http.client

#print("This program returns a list of http methods enabled on a target server...\n")
print("This program returns the status code of a target server...\n")

target = input("Please enter target IP address: ")
uri = input("Please enter the resource: ")
port = int(input("Please enter http port: "))

if port == " ": port = 80

try:
	conn = http.client.HTTPConnection(target,port)
	conn.request('GET', uri)
	#conn.request('OPTIONS', "/")
	resp = conn.getresponse()
	#print(f"The enabled methods are: {resp.getheader('allow')}")
	print(f"Server Response: {resp.status} {resp.reason}")
	conn.close()
except:
	print("Connection refused!")
