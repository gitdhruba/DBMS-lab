import socket
import threading
import random

host = "127.0.0.1"
srverport = 9000
port = random.randint(15000, 18000)
serveraddr = (host, srverport)
clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsock.bind((host, port))

def handle_recv():
    while True:
        msg, _ = clientsock.recvfrom(1024)
        print(msg.decode())


def handle_send():
    while True:
        msg = input(">>> ")
        clientsock.sendto(msg.encode(), serveraddr)


rthr = threading.Thread(target=handle_recv, args=())
sthr = threading.Thread(target=handle_send, args=())
rthr.start()
sthr.start()
