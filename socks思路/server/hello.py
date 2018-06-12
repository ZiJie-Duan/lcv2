import socket
import time

host = ""
port = 2233

sock = socket.socket()

sock.bind((host, port))

sock.listen(5)

while True:
    cli, addr = sock.accept()
    print(addr)
    while True:
        data = cli.recv(1024).decode()
        if not data:
            break
        print(data)
        sen = "ok!"
        cli.sendall(sen.encode())
    cli.close()
