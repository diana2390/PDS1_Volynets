import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as k:
    k.connect(("localhost", 57000))
    while True:
        c = input("Client: ").encode()
        k.send(c)
        data = k.recv(1024)
        print(f"Server`s message: {data.decode()}")