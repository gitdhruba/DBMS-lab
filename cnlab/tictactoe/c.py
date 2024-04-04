import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 12334
client.connect((host, port))

while(True):
    resp=client.recv(1024).decode('utf-8')
    print(resp)
    if(resp=="end"):
        break
    data=input(">> ")
    client.send(data.encode('utf-8'))