import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.bind(('', 57000))
    f.listen(10)
    print("Server is running")
    conn, addr = f.accept()
    while True:
        data = conn.recv(1024).decode()
        print(f"Client`s message: {data}")
        a = input("Server: ")
        conn.send(a.encode())