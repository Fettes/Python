# Import the socket package
import socket
from datetime import time

# create a socket

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
    s.send(command_list[i].encode('utf-8'))
    time.sleep(0.25)
s.close()