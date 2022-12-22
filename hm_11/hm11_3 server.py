import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser:
ser.bind(('', 59000))
ser.listen(10)
print("Server is running")
conn, addr = ser.accept()
while True:
    # print("connected:", addr)
    data = conn.recv(1024).decode()
    punc = ",.!?:; "
    for i in punc:
        data = data.replace(i, "")
    data = str(len(data))
    conn.send(data.encode())