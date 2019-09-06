# Import the socket package
import socket

# create a socket
import time

s = socket.socket()
# connect the server
s.connect(('192.168.200.52', 19002))  # ①
# Define the command list
command_list = ["Tianshi Feng","look","look chest","look mirror","get hairpin",
                "unlock chest with hairpin","open chest","look in chest","unlock door with hairpin",
                "open door"]
for i in command_list:
    res = s.recv(1024)
    print(res.decode('utf-8'))
    s.send(i.encode('utf-8'))
    time.sleep(0.25)
res_suc = s.recv(1024)
print(res_suc.decode('utf-8'))
s.close()