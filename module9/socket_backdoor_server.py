import socket
ip="10.0.2.15"
port=8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_PEUSEADDR,1)
s.bind((ip,port))
s.listen(1)
conn,addr=s.accept()
print('[+]connected to', addr)
conn.send(b"hello")
response=conn.recv(1024)
print(response)