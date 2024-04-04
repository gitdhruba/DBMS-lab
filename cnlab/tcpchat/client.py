import socket
import threading as th

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 7000

client_socket.connect((host,port))

def handle_send(client_socket):
    while True:
        msg = input(">>> ")
        client_socket.send(msg.encode('utf-8'))

def handle_recv(client_socket):
    while True:
        msg = client_socket.recv(1024).decode('utf-8')
        print(msg)

rth = th.Thread(target = handle_recv,args = (client_socket,))
sth = th.Thread(target = handle_send,args = (client_socket,))
rth.start()
sth.start()

#client_socket.close()
