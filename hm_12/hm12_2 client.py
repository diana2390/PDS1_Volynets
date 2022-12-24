import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl:
    cl.connect(("localhost", 51000))
    while True:
        data = input("Enter numbers: ")
        cl.send(data.encode())
        data = cl.recv(1024)
        print(data.decode())