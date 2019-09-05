# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('192.168.56.1', 2048))  # ①
str1 = input("请输入：")
s.send(str1.encode('utf-8'))
print('我刚刚输入的指令是：--%s--' % s.recv(1024).decode('utf-8'))
s.close()
