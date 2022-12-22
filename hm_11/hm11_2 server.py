import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 53000))
    s.listen(10)
    print("Server is running")
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        print(data)
        if data == "I need help":
            conn.send("ok".encode())
        elif data == "I want cookies":
            conn.send("10$".encode())
        else:
            print(f"Client`s message: {data}")
            a = input("Server: ")
            conn.send(a.encode())