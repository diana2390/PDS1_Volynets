import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as r:
    r.connect(("localhost", 59000))
    r.send("Hello, world".encode())
    data = r.recv(1024).decode()
    print(data)