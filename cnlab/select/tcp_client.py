import socket

PORT = 5000

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd.connect(('127.0.0.1', PORT))

message = "Hello Server"
sockfd.send(message.encode())

data = sockfd.recv(1024)
print("Message from server:", data.decode())

sockfd.close()

