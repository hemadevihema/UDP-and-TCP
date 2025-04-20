import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen(1)
print("Server is waiting for connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024).decode()
    if data.lower() == "exit":
        break
    print("Client:", data)
    msg = input("You: ")
    conn.send(msg.encode())

conn.close()
server.close()
