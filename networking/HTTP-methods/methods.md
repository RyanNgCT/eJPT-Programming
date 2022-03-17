Command: 
```
$ nc 192.168.233.134 80
```

**Parameters**

===================================

GET / HTTP/1.1
host: 192.168.233.134

===================================

POST /WebGoat/attack?Screen=64&menu=500 HTTP/1.1
host: 192.168.233.134

Username=test&SUBMIT=Submit

===================================

HEAD / HTTP/1.1
host: 192.168.233.134

===================================

PUT /new.html HTTP/1.1
Host: 192.168.233.134
Content-type: text/html
Content-length: 16

<p>New File</p>

===================================

DELETE /new.html HTTP/1.1
host: 192.168.233.134

===================================

OPTIONS / HTTP/1.1
host: 192.168.233.134
