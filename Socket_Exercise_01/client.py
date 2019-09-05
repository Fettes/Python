# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('192.168.200.116', 2048))    # ①
print('--%s--' % s.recv(1024).decode('utf-8'))
s.close()