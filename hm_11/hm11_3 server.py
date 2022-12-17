import socket
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_socket.bind(('', 59000))
new_socket.listen(10)
print("Server is running")
conn, addr = new_socket.accept()
while True:
    # print("connected:", addr)
    data = conn.recv(1024).decode()
    punc = ",.!?:; "
    for i in punc:
        data = data.replace(i, "")
    data = str(len(data))
    conn.send(data.encode())