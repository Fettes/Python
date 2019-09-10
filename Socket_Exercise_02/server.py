# Import the socket package
import socket

# create a socket
s = socket.socket()
# bind IP and the Port
s.bind(('192.168.56.1', 2048))
# Listen to the connection
s.listen()
while True:
    # Start the server and accept the connection
    c, addr = s.accept()
    # print('Connection address：', addr)
    while True:
        try:
            c_l = c.recv(1024)
        except Exception:
            print("The broken connection", addr)
            break
        command_line = c_l.decode('utf-8')
        print("The command from client:", command_line)
        c.send(command_line.encode('utf-8'))
    # Close the connection
    c.close()
    # c.send('您好，您收到了服务器的新年祝福！'.encode('utf-8'))
    # 关闭连接
    # c.close()
