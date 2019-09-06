# Import the socket package
import socket

# create a socket
s = socket.socket()
# connect the server
s.connect(('192.168.200.52', 19002))  # ①
while True:
    str1 = input('>>').strip()
    if not str1:
        break
    s.send(str1.encode('utf-8'))
    res = s.recv(1024)
    print('My command is：%s' % res.decode('utf-8'))
s.close()