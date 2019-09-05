# 导入 socket 模块
import socket

# 创建socket对象
s = socket.socket()
# 将socket绑定到本机IP和端口
s.bind(('192.168.56.1', 2048))
# 服务端开始监听来自客户端的连接
s.listen()
while True:
    # 每当接收到客户端socket的请求时，该方法返回对应的socket和远程地址
    c, addr = s.accept()
    # print(c)
    # print('连接地址：', addr)
    msg = c.recv(1024)
    message = msg.decode('utf-8')
    print(message)
    c.send(message.encode('utf-8'))
    # c.send('您好，您收到了服务器的新年祝福！'.encode('utf-8'))
    # 关闭连接
    c.close()