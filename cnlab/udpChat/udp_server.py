import socket
import threading

host = "127.0.0.1"
port = 9000
srvrsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvrsock.bind((host, port))

clients = set()

def broadcast_message(msg, addr):
    sndmsg = f"{addr} : {msg}"
    for client in clients:
        srvrsock.sendto(sndmsg.encode(), client)


def handle_client(msg, addr):
    if addr not in clients:
        clients.add(addr)

    broadcast_message(msg, addr)


while True:
    msg, addr = srvrsock.recvfrom(1024)
    threading.Thread(target=handle_client, args=(msg.decode(), addr, )).start()