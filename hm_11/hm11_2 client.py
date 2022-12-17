import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 53000))
while True:
    c = input("Client: ").encode()
    client.send(c)
    data = client.recv(1024)
    print(f"Server`s answer: {data.decode()}")