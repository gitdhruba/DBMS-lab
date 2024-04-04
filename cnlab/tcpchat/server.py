import socket
import threading as th

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 7000

server_socket.bind((host,port))

server_socket.listen(10)
print(f"Server listening on {host} : {port}")
clients = {}

def handle_client(client_socket,client_name):

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            broadcast_msg(f"{client_name} : {data}")

        except ConnectionResetError:
            break
    del clients[client_name]
    client_socket.close()
    broadcast_msg(f"{client_name} has left the chat")

def broadcast_msg(msg):
    for client_socket in clients.values():
        try:
            client_socket.send(msg.encode('utf-8'))
        except ConnectionResetError:
            pass

while True:
    conn, client_name = server_socket.accept()
    broadcast_msg(f"{client_name} joined the chat!!")
    clients[client_name] = conn
    cthr = th.Thread(target = handle_client, args = (conn,client_name))
    cthr.start()

server_socket.close()
