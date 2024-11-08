# echo-client.py

import socket
import sys, select

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        i, o, e = select.select( [sys.stdin], [], [], 0.01 )
        #key = input('press key')
        if (i):
            command = sys.stdin.readline().strip()
            s.sendall(command.encode())
        else:
            s.sendall(b" ")
#    data = s.recv(1024)

print(f"Received {data!r}")

