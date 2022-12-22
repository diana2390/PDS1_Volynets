import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as y:
    y.connect(("localhost", 53000))
    while True:
        c = input("Client: ").encode()
        y.send(c)
        data = y.recv(1024)
        print(f"Server`s answer: {data.decode()}")