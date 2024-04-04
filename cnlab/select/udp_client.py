import socket

PORT = 5001

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello Server"
sockfd.sendto(message.encode('utf-8'), ('127.0.0.1', PORT))

data, addr = sockfd.recvfrom(1024)
print("Message from server:", data.decode())

sockfd.close()

