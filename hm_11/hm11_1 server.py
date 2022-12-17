import socket
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_socket.bind(('', 57000))
new_socket.listen(10)
print("Server is running")
conn, addr = new_socket.accept()
while True:
    data = conn.recv(1024).decode()
    print(f"Client`s message: {data}")
    a = input("Server: ")
    conn.send(a.encode())