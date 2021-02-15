#!/usr/bin/python

import socket

host = "127.0.0.1" # The server's hostname or IP address
#host = "itss.biomea.com"
port = 80        # The port used by the server
#create a socket object
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the client
client.connect((host,port))
#send data
client.send("GET /cgi-bin/echo.cgi HTTPS/1.1\r\nHost: itss.biomea.com\r\n\r\n")
# receive some data
response = client.recv(4096)
print response

