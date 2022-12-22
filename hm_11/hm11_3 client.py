import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl:
    cl.connect(("localhost", 59000))
    cl.send("Hello, world".encode())
    data = cl.recv(1024).decode()
    print(data)