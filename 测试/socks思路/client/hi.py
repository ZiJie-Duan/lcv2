import socket
import time

sock = socket.socket()

HOST = '45.32.169.9'
PORT = 2233
data = input("密钥：")


sock.connect((HOST, PORT))

sock.sendall(data.encode())
data = sock.recv(1024).decode()
print(data)

sock.close()

input()
